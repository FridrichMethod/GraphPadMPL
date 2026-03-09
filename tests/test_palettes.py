"""Tests for mplplots.palettes."""

from mplplots.palettes import CUSTOM, CUSTOM_CYCLE


class TestPalettes:
    def test_custom_has_eleven_colors(self) -> None:
        assert len(CUSTOM) == 11

    def test_custom_colors_are_hex_strings(self) -> None:
        for color in CUSTOM:
            assert color.startswith("#")
            assert len(color) == 7

    def test_custom_cycle_iterates(self) -> None:
        colors = [next(CUSTOM_CYCLE) for _ in range(3)]
        assert len(colors) == 3
        assert all(c.startswith("#") for c in colors)
