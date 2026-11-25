"""Hand-written bank of synthetic tasks: publishable cards and non-publishable distractors."""

from importlib import import_module

CARD_MODULES = ["cards_hardware", "cards_software", "cards_ia", "cards_innovacion", "cards_mixed",
                "cards_set2_a", "cards_set2_b"]

CARDS: list[dict] = []
for _name in CARD_MODULES:
    try:
        CARDS += import_module(f"{__name__}.{_name}").CARDS
    except ModuleNotFoundError:
        pass

from .nonpub import NONPUB as _NONPUB_1  # noqa: E402
from .nonpub_set2 import NONPUB as _NONPUB_2  # noqa: E402

NONPUB: list[dict] = _NONPUB_1 + _NONPUB_2

_ids = [c["id"] for c in CARDS] + [n["id"] for n in NONPUB]
assert len(_ids) == len(set(_ids)), "duplicate ids in the bank"
