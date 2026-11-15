"""Hand-written bank of synthetic tasks: publishable cards and non-publishable distractors."""

from importlib import import_module

CARD_MODULES = ["cards_hardware", "cards_software", "cards_ia", "cards_innovacion", "cards_mixed"]

CARDS: list[dict] = []
for _name in CARD_MODULES:
    try:
        CARDS += import_module(f"{__name__}.{_name}").CARDS
    except ModuleNotFoundError:
        pass

from .nonpub import NONPUB  # noqa: E402

_ids = [c["id"] for c in CARDS] + [n["id"] for n in NONPUB]
assert len(_ids) == len(set(_ids)), "duplicate ids in the bank"
