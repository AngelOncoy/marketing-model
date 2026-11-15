"""Rule-based validators, ported from the ideas of the ERP's Propuestas IA checks (estudio s. 8.1).

Used both as dataset filters and as evaluation metrics. Each check returns a list of error strings.
"""

from __future__ import annotations

import re
from typing import Iterable

from marketing_model.generate.bank.context import CLIENTS, PERSONS

ISSUE = re.compile(r"#\d+\b")
ROUTE = re.compile(r"(?<![\w.])/(?:[\w\-{}]+/)+[\w\-{}.]*")
PLACEHOLDER = re.compile(r"\[[A-Z_]+\d*\]")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"\b9\d{8}\b")
SNAKE = re.compile(r"\b[a-z]+_[a-z0-9_]+\b")
UPPER_SNAKE = re.compile(r"\b[A-Z]{2,}_[A-Z0-9_]+\b")
NUMBER = re.compile(r"\d+(?:[.,]\d+)?")

FORBIDDEN_IN_COPY = ["vulnerab", "hotfix", "endpoint", "issue", "pull request", "en progreso",
                     "en revisión", "horas de desarrollo", ".env", "api key"]
EXAGGERATIONS = ["100 %", "100%", "garantiza", "el mejor", "la mejor", "los mejores", "revolucion",
                 "líder", "nunca falla", "totalmente seguro", "siempre seguro", "sin errores",
                 "perfect", "único en", "increíble", "infalible"]
NO_TEXT_CLAUSE = "No text, no letters, no logos"


def strings(obj) -> Iterable[str]:
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def leaks(report: str, output: dict) -> list[str]:
    """Internal tokens from the report (or known names) that reappear anywhere in the output."""
    text = "\n".join(strings(output))
    errors = []
    for pat in (ISSUE, ROUTE, PLACEHOLDER, EMAIL, PHONE, SNAKE, UPPER_SNAKE):
        for tok in set(pat.findall(report)):
            if tok in text:
                errors.append(f"leak: {tok}")
    for pat in (ISSUE, PLACEHOLDER, EMAIL, PHONE):
        for tok in set(pat.findall(text)) - {e.split(': ', 1)[1] for e in errors}:
            errors.append(f"leak-pattern: {tok}")
    for name in CLIENTS + PERSONS:
        if name.lower() in text.lower():
            errors.append(f"leak-name: {name}")
    return errors


def public_text(p: dict) -> list[str]:
    """Everything a reader of the post would see."""
    c, t = p["copys"], p["pieza"]["textos"]
    out = [c["linkedin"], c["facebook"], c["instagram"], t["titulo"], *t["bullets"], t["dato"] or "", t["cta"]]
    out += [s["voz"] for s in p["guion_tiktok"]]
    out += [d["titulo"] + " " + d["texto"] for d in p["pieza"]["diapositivas"]]
    return out


def figures(report: str, p: dict) -> list[str]:
    """Every multi-digit figure in the public text must appear in the report."""
    src = {n.replace(",", ".") for n in NUMBER.findall(report)}
    errors = []
    for s in public_text(p):
        for n in NUMBER.findall(s):
            if len(n.replace(",", "").replace(".", "")) < 2:
                continue
            if n.replace(",", ".") not in src:
                errors.append(f"figure not in report: {n}")
    return errors


def wording(p: dict) -> list[str]:
    errors = []
    low = "\n".join(public_text(p)).lower()
    errors += [f"forbidden term: {w}" for w in FORBIDDEN_IN_COPY if w in low]
    errors += [f"exaggeration: {w}" for w in EXAGGERATIONS if w in low]
    return errors


def tags(p: dict, brand_tag: str) -> list[str]:
    errors = []
    for net, lst in p["hashtags"].items():
        if brand_tag not in lst:
            errors.append(f"{net}: missing {brand_tag}")
        if len(lst) != len(set(t.lower() for t in lst)):
            errors.append(f"{net}: duplicated hashtag")
        errors += [f"{net}: bad hashtag {t}" for t in lst if not re.fullmatch(r"#\w+", t)]
    return errors


def piece(p: dict) -> list[str]:
    errors = []
    t = p["pieza"]["textos"]
    if len(t["titulo"].split()) > 6:
        errors.append(f"title > 6 words: {t['titulo']}")
    errors += [f"bullet > 4 words: {b}" for b in t["bullets"] if len(b.split()) > 4]
    if NO_TEXT_CLAUSE not in p["pieza"]["prompt_imagen"]:
        errors.append("image prompt lacks the no-text clause")
    hooks = {"linkedin": 150, "instagram": 125}
    for net, limit in hooks.items():
        first = p["copys"][net].split("\n")[0]
        if len(first) > limit:
            errors.append(f"{net} hook > {limit} chars")
    return errors


def validate(report: str, output: dict, brand_tag: str = "#CorAll") -> list[str]:
    errors = leaks(report, output)
    p = output.get("propuesta")
    if p:
        errors += figures(report, p) + wording(p) + tags(p, brand_tag) + piece(p)
    return errors
