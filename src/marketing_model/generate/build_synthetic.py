"""Assemble synthetic daily reports and their target proposals from the hand-written bank.

The bank (generate/bank/) holds the creative content: publishable tasks with their copy (cards)
and non-publishable tasks (distractors). This script composes reports in CorAll's real format,
mixes cards with distractors, varies the design brief and writes one JSONL row per report.

Usage: python -m marketing_model.generate.build_synthetic --n 500 --seed 42
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from datetime import date, timedelta
from pathlib import Path

from marketing_model.brand import ROOT, load_brand, short_kit
from marketing_model.generate.bank import CARDS, NONPUB
from marketing_model.generate.bank.context import (
    BLOQUEOS, CLIENTS, CLIENTS_BY_SECTOR, DISCARD_PHRASES, ERP_ASSISTANT_PROJECT, IN_PROGRESS_REASON,
    INTERNAL_PROJECTS, NONPUB_SECTOR, PENDIENTES, PERSONS, client_project,
)
from marketing_model.generate.bank.wip import WIP_DET

VERSION = "0.2"
OUT = ROOT / "data" / "synthetic" / f"synthetic_v{VERSION}.raw.jsonl"

INSTRUCTION = (
    "Eres el asistente de marketing de CorAll. Lee el kit de marca y el reporte diario de desarrollo. "
    "Evalúa cada tarea y decide si hay algo publicable. Si lo hay, elige la mejor idea y devuelve la "
    "propuesta en JSON con el copy por red, hashtags, guion de TikTok y brief de la pieza. Si no hay "
    "nada publicable, descarta y explica el motivo. Nunca incluyas información interna: rutas, issues, "
    "PR, nombres de clientes o personas, riesgos, bloqueos ni horas."
)

DONE = ["Terminado (desplegado)", "Terminado (en producción)", "Desplegado"]
NOT_DONE = ["En progreso", "En revisión"]

RESOLUTION = {"4:5": "1080x1350", "1:1": "1080x1080", "1.91:1": "1200x627"}

BACKGROUNDS = {
    "gris claro con ola roja": ("light", "light grey background with a soft red wave at the bottom"),
    "blanco con formas geométricas rojas y negras": ("light", "white background with red and black geometric shapes on the edges"),
    "foto con overlay rojo": ("dark", "photographic background with a translucent red overlay"),
    "negro con patrón de circuito": ("dark", "near-black background with a subtle continuous circuit pattern"),
    "blanco con patrón de circuito sutil": ("light", "white background with a very subtle grey circuit line pattern"),
}
FOOTERS = {
    "light": ["rojo con logo blanco", "negro con tres íconos", "negro con 'Desarrollado por CorAll'", "mixto rojo y negro"],
    "dark": ["blanco con logo negro", "rojo con logo blanco", "mixto rojo y negro"],
}
LOGO = {
    "light": ["logo negro arriba a la izquierda", "logo negro junto al título", "isotipo arriba a la derecha"],
    "dark": ["logo blanco arriba a la izquierda", "logo blanco centrado abajo", "isotipo arriba a la derecha"],
}
# The brief's visual is read from the card's image description, so the brief and the image prompt agree.
VISUAL_KEYWORDS = [
    ("mockup", "mockup de interfaz"),
    ("3d illustration", "ilustración 3D"),
    ("3d render", "render 3D del producto"),
    ("icons", "ilustración de íconos de línea"),
    ("lineup", "foto de producto en estudio"),
    ("split", "composición dividida en dos escenas"),
]


def visual_of(card: dict) -> str:
    if card.get("vis_es"):
        return card["vis_es"]
    if card.get("adj", "ninguna") != "ninguna":
        return f"foto adjunta de {card['adj']} con overlay de marca"
    vis = card["vis"].lower()
    return next((es for key, es in VISUAL_KEYWORDS if key in vis), "fotografía realista de la escena")


def composition_of(card: dict, rng: random.Random) -> str:
    """Only layouts the card's content can fill: before/after, timeline and quote need a card's own `comp`."""
    if card.get("comp"):
        return card["comp"]
    if card["pilar"] == "evento":
        return "fecha, hora y lugar con íconos"
    options = [f"lista de {len(card['bul'])} beneficios"]
    if card["dato"]:
        options.append("dato destacado")
    if card["pilar"] == "catalogo":
        options.append("grilla")
    return rng.choice(options)
GENERIC_TAGS = {
    "software": ["#DesarrolloDeSoftware", "#TransformaciónDigital", "#SoftwareAMedida"],
    "hardware": ["#IoT", "#Electrónica", "#HardwareAMedida"],
    "ia": ["#InteligenciaArtificial", "#VisiónArtificial", "#IA"],
    "innovacion": ["#Innovación", "#TransformaciónDigital", "#Industria40"],
}
PLACE_TAGS = ["#Trujillo", "#Perú", "#TecnologíaPeruana", "#LaLibertad"]
CAROUSEL_PILARS = {"educativo": 0.6, "catalogo": 0.6, "hito": 0.3, "servicio_territorio": 0.3}


class Namer:
    """Per-report names: anonymizer placeholders (60 %) or fictitious names that slipped through (40 %).

    Each mention gets a new entity, as distinct tasks usually refer to different clients or people.
    A fictitious client is taken from the task's sector, so a farm task never names a shoe maker.
    """

    def __init__(self, rng: random.Random):
        self.rng = rng
        self.placeholders = rng.random() < 0.6
        self.n = {"CLIENTE": 0, "PERSONA": 0}
        self.used: set[str] = set()
        self.persons = rng.sample(PERSONS, len(PERSONS))

    def next(self, kind: str, sector: str | None = None) -> str:
        self.n[kind] += 1
        if self.placeholders:
            return f"[{kind}_{self.n[kind]}]"
        if kind == "PERSONA":
            return self.persons[(self.n[kind] - 1) % len(self.persons)]
        pools = [CLIENTS_BY_SECTOR[sector]] if sector else []
        pools.append(CLIENTS)
        for pool in pools:
            free = [c for c in pool if c not in self.used]
            if free:
                name = self.rng.choice(free)
                self.used.add(name)
                return name
        return self.rng.choice(pools[0])

    def fill(self, text: str, sector: str | None = None) -> str:
        while "{cliente}" in text:
            text = text.replace("{cliente}", self.next("CLIENTE", sector), 1)
        while "{persona}" in text:
            text = text.replace("{persona}", self.next("PERSONA"), 1)
        return text


def sector_of(item: dict) -> str | None:
    return item.get("sector") if "li" in item else NONPUB_SECTOR.get(item["id"])


def detail(item: dict, estado: str) -> str:
    """Unfinished cards use their unfinished text so the state and the detail agree."""
    if "li" in item and estado in NOT_DONE:
        return WIP_DET[item["id"]]
    return item["det"]


def matrix_row(item: dict, estado: str, rng: random.Random, namer: Namer) -> str:
    issue = f"#{rng.randint(12, 480)}"
    pr = f"#{rng.randint(5, 260)}" if rng.random() < 0.8 else "-"
    hours = rng.choice([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6])
    det = namer.fill(detail(item, estado), sector_of(item))
    return f"| {item['mod']} | {issue} | {pr} | {estado} | {hours} | {det} |"


def render_report(day: date, project: str, rows: list[tuple[dict, str]], rng: random.Random) -> str:
    namer = Namer(rng)
    fill = namer.fill
    matrix = [(it, st) for it, st in rows if it["sec"] == "matriz"]
    annex = [(it, st) for it, st in rows if it["sec"] == "anexado"]
    lines = [f"# Reporte diario - {day.isoformat()}", "",
             f"**Desarrollador:** {namer.next('PERSONA')}", f"**Proyecto principal:** {project}", "",
             "## Matriz", ""]
    if matrix:
        lines += ["| Módulo/Repo | Issue | PR | Estado | Horas | Detalle |", "|---|---|---|---|---|---|"]
        lines += [matrix_row(it, st, rng, namer) for it, st in matrix]
    else:
        lines.append("Sin cambios de código hoy.")
    lines += ["", "## Anexado", ""]
    if annex:
        lines += [f"- {fill(it['det'], sector_of(it))} ({st})" for it, st in annex]
    else:
        lines.append("- Revisión de correos y coordinación del equipo.")
    lines += ["", "## Pendientes", ""]
    lines += [f"- {fill(p)}" for p in rng.sample(PENDIENTES, rng.randint(1, 3))]
    lines += ["", "## Bloqueos / Riesgos", ""]
    lines.append(f"- {fill(rng.choice(BLOQUEOS))}" if rng.random() < 0.45 else "- Ninguno.")
    return "\n".join(lines)


def idea_from_nonpub(item: dict) -> dict:
    return {"fuente": item["fuente"], "pilar": item["pilar"], "valor": item["valor"],
            "riesgo": item["riesgo"], "publicable": False, "razon": item["razon"]}


def idea_from_card(card: dict, done: bool) -> dict:
    if done:
        return {"fuente": card["fuente"], "pilar": card["pilar"], "valor": card["valor"],
                "riesgo": card.get("riesgo", 1), "publicable": True, "razon": card["razon"]}
    return {"fuente": card["fuente"], "pilar": card["pilar"], "valor": card["valor"], "riesgo": 4,
            "publicable": False, "razon": IN_PROGRESS_REASON}


def hashtags(card: dict, rng: random.Random, brand: dict) -> dict:
    mark = brand["hashtag_marca"]
    topic = [t for t in card["tags"] if t != mark]
    pool = topic + [t for t in GENERIC_TAGS[card["area"]] if t not in topic]
    li = [mark] + topic[: rng.randint(2, 4)]
    ig_extra = pool + [t for t in PLACE_TAGS if t not in pool]
    ig = [mark] + ig_extra[: rng.randint(4, 7)]
    tt = [mark] + topic[: rng.randint(2, 3)]
    return {"linkedin": li, "instagram": ig, "tiktok": tt}


def slogan(card: dict, rng: random.Random, brand: dict) -> str:
    options = [s for s in brand["esloganes"] if "agroindustria" not in s]
    if card.get("sector") == "agroindustria":
        options.append(next(s for s in brand["esloganes"] if "agroindustria" in s))
    return rng.choice(options)


def image_prompt(card: dict, bg_en: str, brand: dict) -> str:
    p = brand["paleta"]
    if card.get("adj", "ninguna") != "ninguna":
        subject = (f"Use the attached {card['adj']} photo as the main subject without altering it; "
                   f"build around it: {card['vis']}")
    else:
        subject = card["vis"]
    return (f"{subject}. {bg_en}. Brand palette: deep red {p['rojo']}, near-black {p['negro']} and "
            f"white {p['blanco']}. Clean, professional composition with empty space reserved for the "
            "title and footer. No text, no letters, no logos, no recognizable faces.")


def slides(card: dict, cta: str) -> list[dict]:
    first = card["ig"].strip().split("\n")[0]
    out = [{"titulo": card["tit"], "texto": first, "visual": "visual principal del tema con fondo de marca"}]
    for label, text in card["bul"]:
        out.append({"titulo": label, "texto": text, "visual": f"ícono de línea sobre círculo rosa suave: {label.lower()}"})
    out.append({"titulo": "En resumen", "texto": card["dato"] or card["fb"].strip().split("\n")[0],
                "visual": "dato o resumen destacado en rojo de marca"})
    out.append({"titulo": cta, "texto": "Escríbenos por mensaje directo y cuéntanos tu caso.",
                "visual": "logo CorAll centrado sobre fondo rojo de marca"})
    return out


def proposal(card: dict, rng: random.Random, brand: dict) -> dict:
    pilar = card["pilar"]
    bg = rng.choice(list(BACKGROUNDS))
    tone, bg_en = BACKGROUNDS[bg]
    if card.get("adj") in {"campo", "equipo"}:
        bg, (tone, bg_en) = "foto con overlay rojo", BACKGROUNDS["foto con overlay rojo"]
    carousel = rng.random() < CAROUSEL_PILARS.get(pilar, 0.0)
    ratio = "4:5" if carousel else rng.choices(["4:5", "1:1", "1.91:1"], [6, 2, 2])[0]
    visual = visual_of(card)
    comp = composition_of(card, rng)
    cta = card.get("cta", "Conoce más")
    return {
        "pilar": pilar,
        "area": card["area"],
        "tipo_proyecto": card["tipo"],
        "copys": {"linkedin": card["li"].strip(), "facebook": card["fb"].strip(), "instagram": card["ig"].strip()},
        "hashtags": hashtags(card, rng, brand),
        "guion_tiktok": [{"segundos": s, "toma": t, "voz": v}
                         for s, (t, v) in zip(["0-3", "3-9", "9-15", "15-20"], card["tt"])],
        "pieza": {
            "formato": "carrusel" if carousel else "imagen_unica",
            "ratio": ratio,
            "resolucion": RESOLUTION[ratio],
            "estilo": {"fondo": bg, "footer": rng.choice(FOOTERS[tone]), "logo": rng.choice(LOGO[tone]),
                       "visual": visual, "composicion": comp, "cta": cta},
            "textos": {"titulo": card["tit"], "bullets": [b for b, _ in card["bul"]], "dato": card["dato"],
                       "cta": cta, "eslogan": slogan(card, rng, brand)},
            "diapositivas": slides(card, cta) if carousel else [],
            "imagen_adjunta": card.get("adj", "ninguna"),
            "prompt_imagen": image_prompt(card, bg_en, brand),
        },
    }


def discard_reason(items: list[dict], has_wip: bool) -> str:
    cats = []
    for it in items:
        if it["cat"] not in cats:
            cats.append(it["cat"])
    phrases = [DISCARD_PHRASES[c] for c in cats]
    if has_wip:
        phrases.insert(0, DISCARD_PHRASES["progreso"])
    return "No hay contenido publicable hoy: " + "; ".join(dict.fromkeys(phrases)) + "."


def companions(area: str, k: int, rng: random.Random, exclude: set[str]) -> list[dict]:
    same = [n for n in NONPUB if n["area"] == area and n["id"] not in exclude]
    other = [n for n in NONPUB if n["area"] != area and n["id"] not in exclude]
    out = []
    for _ in range(k):
        pool = same if (same and rng.random() < 0.7) else other
        choice = rng.choice(pool)
        pool.remove(choice)
        out.append(choice)
    return out


def nonpub_state(item: dict, rng: random.Random) -> str:
    if item["cat"] == "progreso":
        return rng.choice(NOT_DONE)
    return item.get("estado") or (rng.choice(DONE) if item["sec"] == "matriz" else "Realizado")


def card_state(card: dict, done: bool, rng: random.Random) -> str:
    if card["sec"] == "anexado":
        return "Realizado"
    return rng.choice(DONE) if done else rng.choice(NOT_DONE)


def project_of(card: dict | None, area: str, rng: random.Random) -> str:
    """Main project that fits the lead task: its client sector, or the area's internal project."""
    if card is None:
        if rng.random() < 0.5:
            return INTERNAL_PROJECTS[area]
        return client_project(area, rng.choice(list(CLIENTS_BY_SECTOR)))
    if card["tipo"] == "cliente":
        return client_project(area, card["sector"])
    if area == "ia" and card.get("vis_es") == "mockup de interfaz":
        return ERP_ASSISTANT_PROJECT
    return INTERNAL_PROJECTS[area]


def build_row(kind: str, card: dict | None, area: str, rng: random.Random, day: date, brand: dict,
              idx: int) -> dict:
    rows: list[tuple[dict, str]] = []
    ideas: list[dict] = []
    k = rng.choices([0, 1, 2, 3], [2, 4, 3, 1])[0] if kind == "publish" else rng.choices([1, 2, 3], [3, 4, 3])[0]
    distractors = companions(area, k, rng, set())
    if kind in {"publish", "wip"}:
        done = kind == "publish"
        rows.append((card, card_state(card, done, rng)))
        ideas.append(idea_from_card(card, done))
    for d in distractors:
        rows.append((d, nonpub_state(d, rng)))
        ideas.append(idea_from_nonpub(d))
    order = list(range(len(rows)))
    rng.shuffle(order)
    rows = [rows[i] for i in order]
    ideas = [ideas[i] for i in order]
    report = render_report(day, project_of(card, area, rng), rows, rng)
    if kind == "publish":
        output = {"decision": "publicar", "motivo_descarte": None, "ideas_evaluadas": ideas,
                  "propuesta": proposal(card, rng, brand)}
    else:
        output = {"decision": "descartar", "motivo_descarte": discard_reason(distractors, kind == "wip"),
                  "ideas_evaluadas": ideas, "propuesta": None}
    group = card["id"] if card else f"d{idx:03d}"
    return {
        "id": f"syn-{idx:04d}",
        "group_id": group,
        "split": split_of(group),
        "meta": {"area": area, "pilar": card["pilar"] if card else None,
                 "tipo_proyecto": card["tipo"] if card else None, "kind": kind,
                 "cats": [d["cat"] for d in distractors]},
        "instruction": INSTRUCTION,
        "input": f"## Kit de marca\n{short_kit(brand)}\n\n## Reporte\n{report}",
        "output": json.dumps(output, ensure_ascii=False),
    }


def split_of(group: str) -> str:
    """Stable split per group: every variant of a report lands in the same split."""
    return "val" if int(hashlib.sha256(group.encode()).hexdigest(), 16) % 10 == 0 else "train"


AREAS = ["software", "hardware", "ia", "innovacion"]
DISCARD_RATE = 0.28


def shares(total: int, weights: dict[str, int]) -> dict[str, int]:
    """Split `total` proportionally to `weights` (largest remainder), so every area gets its fair part."""
    s = sum(weights.values())
    raw = {k: total * w / s for k, w in weights.items()}
    out = {k: int(v) for k, v in raw.items()}
    for k in sorted(raw, key=lambda k: raw[k] - out[k], reverse=True)[: total - sum(out.values())]:
        out[k] += 1
    return out


def plan(n: int, rng: random.Random) -> list[tuple[str, dict | None, str]]:
    """Jobs (kind, card, area). Cards are used in full shuffled passes, so no card is published more
    than once per pass; discards are split per area in proportion to its publications, which keeps the
    publish rate equal across areas (D1)."""
    n_discard = round(n * DISCARD_RATE)
    n_publish = n - n_discard
    published: list[dict] = []
    while len(published) < n_publish:
        batch = list(CARDS)
        rng.shuffle(batch)
        published += batch[: n_publish - len(published)]
    jobs = [("publish", c, c["area"]) for c in published]
    per_area = {a: sum(c["area"] == a for c in published) for a in AREAS}
    for area, k in shares(n_discard, per_area).items():
        wip_pool = [c for c in CARDS if c["area"] == area and c["id"] in WIP_DET]
        n_wip = k // 3
        jobs += [("wip", rng.choice(wip_pool), area) for _ in range(n_wip)]
        jobs += [("discard", None, area) for _ in range(k - n_wip)]
    rng.shuffle(jobs)
    return jobs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=500)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", type=Path, default=OUT)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    brand = load_brand()
    start = date(2026, 9, 1)
    rows = []
    for i, (kind, card, area) in enumerate(plan(args.n, rng), 1):
        day = start + timedelta(days=rng.randint(0, 75))
        rows.append(build_row(kind, card, area, rng, day, brand, i))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{len(rows)} rows -> {args.out}")


if __name__ == "__main__":
    main()
