"""Tells the ES Teacher app from the EG Teacher app by its theme.

Both apps are the same Flutter code with the same copy, so nothing in the
accessibility tree says which one is on screen. What differs is the brand theme:
ES Teacher is blue (app bar, bottom nav, buttons ~ rgb(80,128,186)), EG Teacher
is brown (~ rgb(119,77,39)). We read the dominant *coloured* pixel of a
screenshot — whites, greys and near-blacks are skipped, so cards and text don't
count — and classify its hue.
"""
from __future__ import annotations

import io
from collections import Counter

from PIL import Image

ES = "es"
EG = "eg"

# Reference primaries measured on a Pixel 4a (ES 2.5.7, EG 2.5.8).
ES_PRIMARY = (80, 128, 186)
EG_PRIMARY = (119, 77, 39)


def dominant_colour(png: bytes) -> tuple[int, int, int] | None:
    """Most common saturated colour in the screenshot, quantised to steps of 16
    and returned as the bucket centre. None when the screen has no colour."""
    img = Image.open(io.BytesIO(png)).convert("RGB")
    img = img.resize((img.width // 10, img.height // 10))
    buckets: Counter = Counter()
    for r, g, b in img.getdata():
        hi, lo = max(r, g, b), min(r, g, b)
        if hi < 50 or hi - lo < 50:  # near-black or grey/white
            continue
        buckets[(r // 16, g // 16, b // 16)] += 1
    if not buckets:
        return None
    r, g, b = buckets.most_common(1)[0][0]
    return (r * 16 + 8, g * 16 + 8, b * 16 + 8)


def brand_of(rgb: tuple[int, int, int] | None) -> str | None:
    """ES for a blue primary, EG for a brown/orange one, else None."""
    if rgb is None:
        return None
    r, _, b = rgb
    if b - r >= 40:
        return ES
    if r - b >= 40:
        return EG
    return None


def detect(driver) -> tuple[str | None, tuple[int, int, int] | None]:
    """(brand, dominant colour) of what the app is drawing right now."""
    rgb = dominant_colour(driver.get_screenshot_as_png())
    return brand_of(rgb), rgb
