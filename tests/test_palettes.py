"""Tests for mplplots.palettes."""

import re
from itertools import cycle

import pytest

import mplplots.palettes as palettes
from mplplots.palettes import (
    BLUES,
    CUSTOM,
    CUSTOM_CYCLE,
    GREENS,
    GREYS,
    ORANGES,
    PURPLES,
    REDS,
    get_colors,
)

HEX_RE = re.compile(r"^#[0-9a-f]{6}$")

# Every hand-picked 11-color palette and its cycle
CUSTOM_STYLE_PALETTES = [
    "CUSTOM", "PASTEL", "WARM", "COOL", "EARTH",
    "OCEAN", "ROSE", "FOREST", "LAVENDER", "SUNSET", "COASTAL",
    "SPRING", "SUMMER", "AUTUMN", "WINTER",
    "DAWN", "DUSK",
    "CANDY", "SMOKE", "VINTAGE", "NORDIC", "MEADOW", "CORAL", "TROPICAL", "POWDER",
]

# Colormap-derived 8-color palettes
FAMILY_PALETTES = ["BLUES", "GREENS", "REDS", "PURPLES", "ORANGES", "GREYS"]


# ---------------------------------------------------------------------------
# get_colors() API
# ---------------------------------------------------------------------------
class TestGetColors:
    def test_returns_correct_count(self) -> None:
        assert len(get_colors("Blues", 5)) == 5

    def test_single_color(self) -> None:
        result = get_colors("Blues", 1)
        assert len(result) == 1
        assert HEX_RE.match(result[0])

    def test_returns_hex_strings(self) -> None:
        for c in get_colors("viridis", 6):
            assert HEX_RE.match(c), f"{c} is not a valid hex color"

    def test_full_range(self) -> None:
        colors = get_colors("Set2", 8, start=0, end=1)
        assert len(colors) == 8
        assert len(set(colors)) == 8

    def test_custom_range_differs(self) -> None:
        narrow = get_colors("Blues", 3, start=0.3, end=0.5)
        wide = get_colors("Blues", 3, start=0.1, end=0.9)
        assert narrow != wide

    def test_returns_tuple(self) -> None:
        assert isinstance(get_colors("Reds", 3), tuple)

    @pytest.mark.parametrize("cmap", ["Blues", "Greens", "Reds", "Purples", "viridis", "coolwarm"])
    def test_various_colormaps(self, cmap: str) -> None:
        colors = get_colors(cmap, 4)
        assert len(colors) == 4
        for c in colors:
            assert HEX_RE.match(c)

    def test_start_equals_end_single(self) -> None:
        colors = get_colors("Blues", 1, start=0.5, end=0.5)
        assert len(colors) == 1
        assert HEX_RE.match(colors[0])

    def test_large_n(self) -> None:
        colors = get_colors("viridis", 50)
        assert len(colors) == 50
        assert len(set(colors)) == 50


# ---------------------------------------------------------------------------
# Custom-style 11-color palettes
# ---------------------------------------------------------------------------
class TestCustomStylePalettes:
    @pytest.mark.parametrize("name", CUSTOM_STYLE_PALETTES)
    def test_length_is_11(self, name: str) -> None:
        pal = getattr(palettes, name)
        assert len(pal) == 11, f"{name} has {len(pal)} colors, expected 11"

    @pytest.mark.parametrize("name", CUSTOM_STYLE_PALETTES)
    def test_is_tuple_of_str(self, name: str) -> None:
        pal = getattr(palettes, name)
        assert isinstance(pal, tuple)
        for c in pal:
            assert isinstance(c, str)

    @pytest.mark.parametrize("name", CUSTOM_STYLE_PALETTES)
    def test_valid_hex(self, name: str) -> None:
        pal = getattr(palettes, name)
        for c in pal:
            assert HEX_RE.match(c.lower()), f"{name}: {c} is not a valid hex color"

    @pytest.mark.parametrize("name", CUSTOM_STYLE_PALETTES)
    def test_colors_unique(self, name: str) -> None:
        pal = getattr(palettes, name)
        lower = [c.lower() for c in pal]
        assert len(set(lower)) == len(lower), f"{name} has duplicate colors"

    @pytest.mark.parametrize("name", CUSTOM_STYLE_PALETTES)
    def test_cycle_exists(self, name: str) -> None:
        cycle_obj = getattr(palettes, f"{name}_CYCLE")
        assert type(cycle_obj) is type(cycle(""))

    @pytest.mark.parametrize("name", CUSTOM_STYLE_PALETTES)
    def test_cycle_yields_from_palette(self, name: str) -> None:
        pal = getattr(palettes, name)
        cycle_obj = getattr(palettes, f"{name}_CYCLE")
        first = next(cycle_obj)
        assert first in pal

    def test_palettes_are_distinct(self) -> None:
        seen: set[tuple[str, ...]] = set()
        for name in CUSTOM_STYLE_PALETTES:
            pal = tuple(c.lower() for c in getattr(palettes, name))
            assert pal not in seen, f"{name} duplicates another palette"
            seen.add(pal)

    def test_total_count(self) -> None:
        assert len(CUSTOM_STYLE_PALETTES) == 25


# ---------------------------------------------------------------------------
# Colormap-derived family palettes
# ---------------------------------------------------------------------------
class TestFamilyPalettes:
    @pytest.mark.parametrize("name", FAMILY_PALETTES)
    def test_length_is_8(self, name: str) -> None:
        pal = getattr(palettes, name)
        assert len(pal) == 8, f"{name} has {len(pal)} colors, expected 8"

    @pytest.mark.parametrize("name", FAMILY_PALETTES)
    def test_valid_hex(self, name: str) -> None:
        pal = getattr(palettes, name)
        for c in pal:
            assert HEX_RE.match(c), f"{name}: {c} is not a valid hex color"

    @pytest.mark.parametrize("name", FAMILY_PALETTES)
    def test_colors_unique(self, name: str) -> None:
        pal = getattr(palettes, name)
        assert len(set(pal)) == len(pal), f"{name} has duplicate colors"


# ---------------------------------------------------------------------------
# Legacy tests for CUSTOM specifically
# ---------------------------------------------------------------------------
class TestCustomPalette:
    def test_custom_length(self) -> None:
        assert len(CUSTOM) == 11

    def test_custom_hex_format(self) -> None:
        for c in CUSTOM:
            assert HEX_RE.match(c.lower()), f"{c} is not a valid hex color"

    def test_custom_cycle_is_cycle(self) -> None:
        assert type(CUSTOM_CYCLE) is type(cycle(""))

    def test_custom_cycle_yields_colors(self) -> None:
        first = next(CUSTOM_CYCLE)
        assert first.startswith("#")
