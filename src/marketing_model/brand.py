"""Brand kit loader. Colors, fonts and slogans are read from brand/brand.json, never hard-coded."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BRAND_PATH = ROOT / "brand" / "brand.json"


@lru_cache
def load_brand(path: Path = BRAND_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def short_kit(brand: dict | None = None) -> str:
    """Short brand kit placed in every dataset input."""
    b = brand or load_brand()
    p = b["paleta"]
    return "\n".join([
        f"Marca: {b['empresa']} ({b['ciudad']}). Áreas: {', '.join(b['areas'])}.",
        f"Sectores: {', '.join(b['sectores'])}.",
        f"Colores: rojo {p['rojo']}, negro {p['negro']}, blanco {p['blanco']}; acento opcional {p['marron']}.",
        f"Eslóganes: {'; '.join(b['esloganes'])}.",
        f"Tono: {b['tono']}.",
        f"Nunca publicar: {'; '.join(b['temas_prohibidos'])}.",
        f"Hashtag de marca: {b['hashtag_marca']}.",
    ])
