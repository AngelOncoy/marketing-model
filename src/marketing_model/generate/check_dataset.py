"""Validate, deduplicate and describe a raw synthetic file. Writes the clean file and its card stats.

Usage: python -m marketing_model.generate.check_dataset data/synthetic/synthetic_v0.1.raw.jsonl
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from pydantic import ValidationError

from marketing_model.schema import Output
from marketing_model.validators import validate


def report_of(row: dict) -> str:
    return row["input"].split("## Reporte\n", 1)[1]


def shingles(text: str, k: int = 5) -> set[str]:
    t = " ".join(text.lower().split())
    return {t[i:i + k] for i in range(max(1, len(t) - k + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 1.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("raw", type=Path)
    ap.add_argument("--near", type=float, default=0.9, help="near-duplicate Jaccard threshold")
    args = ap.parse_args()
    rows = [json.loads(l) for l in args.raw.read_text(encoding="utf-8").splitlines() if l.strip()]

    removed: Counter = Counter()
    errors_seen: Counter = Counter()
    kept, seen_hash, kept_sh = [], set(), []
    for r in rows:
        if not r["input"].strip() or not r["output"].strip():
            removed["vacía"] += 1
            continue
        try:
            out = json.loads(r["output"])
            Output.model_validate(out)
        except (json.JSONDecodeError, ValidationError) as e:
            removed["esquema inválido"] += 1
            errors_seen[f"schema: {str(e).splitlines()[0]}"] += 1
            continue
        errs = validate(report_of(r), out)
        if errs:
            reason = "fuga de información" if any(e.startswith("leak") for e in errs) else "validador de copy"
            removed[reason] += 1
            errors_seen.update(errs)
            print(r["id"], r["group_id"], errs)
            continue
        h = hashlib.sha256((r["input"] + r["output"]).encode()).hexdigest()
        if h in seen_hash:
            removed["duplicado exacto"] += 1
            continue
        sh = shingles(report_of(r))
        if any(g != r["group_id"] and jaccard(sh, s) >= args.near for g, s in kept_sh):
            removed["casi duplicado"] += 1
            continue
        seen_hash.add(h)
        kept_sh.append((r["group_id"], sh))
        kept.append(r)

    clean = args.raw.with_name(args.raw.name.replace(".raw", ""))
    with clean.open("w", encoding="utf-8", newline="\n") as f:
        for r in kept:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    def count(key):
        return dict(Counter(key(r) for r in kept).most_common())

    def rate(area):
        sub = [r for r in kept if r["meta"]["area"] == area]
        pub = sum(r["meta"]["kind"] == "publish" for r in sub)
        return round(pub / len(sub), 3) if sub else None

    areas = sorted({r["meta"]["area"] for r in kept})
    stats = {
        "archivo": clean.name,
        "filas_generadas": len(rows),
        "filas_limpias": len(kept),
        "eliminadas_por_motivo": dict(removed),
        "grupos": len({r["group_id"] for r in kept}),
        "por_split": count(lambda r: r["split"]),
        "por_decision": count(lambda r: "publicar" if r["meta"]["kind"] == "publish" else "descartar"),
        "por_tipo_de_fila": count(lambda r: r["meta"]["kind"]),
        "por_area": count(lambda r: r["meta"]["area"]),
        "por_pilar": count(lambda r: r["meta"]["pilar"] or "-"),
        "por_tipo_proyecto": count(lambda r: r["meta"]["tipo_proyecto"] or "-"),
        "tasa_publicacion_por_area": {a: rate(a) for a in areas},
        "errores_detectados": dict(errors_seen.most_common(20)),
        "chars_promedio_input": round(sum(len(r["input"]) for r in kept) / max(1, len(kept))),
        "chars_promedio_output": round(sum(len(r["output"]) for r in kept) / max(1, len(kept))),
    }
    stats_path = clean.with_name(clean.stem + ".ficha.json")
    stats_path.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
