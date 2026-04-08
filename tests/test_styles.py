"""Tests for mplplots styles."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

STYLES_DIR = Path(__file__).resolve().parent.parent / "src" / "mplplots" / "styles"


class TestGraphPadPrismStyle:
    def test_style_file_exists(self) -> None:
        assert (STYLES_DIR / "GraphPadPrism.mplstyle").is_file()

    def test_style_is_loadable(self) -> None:
        style_path = str(STYLES_DIR / "GraphPadPrism.mplstyle")
        plt.style.use(style_path)

    def test_style_sets_dpi(self) -> None:
        style_path = str(STYLES_DIR / "GraphPadPrism.mplstyle")
        plt.style.use(style_path)
        assert matplotlib.rcParams["figure.dpi"] == 300

    def test_style_hides_top_right_spines(self) -> None:
        style_path = str(STYLES_DIR / "GraphPadPrism.mplstyle")
        plt.style.use(style_path)
        assert matplotlib.rcParams["axes.spines.top"] is False
        assert matplotlib.rcParams["axes.spines.right"] is False

    def test_style_applies_to_plot(self) -> None:
        style_path = str(STYLES_DIR / "GraphPadPrism.mplstyle")
        with plt.style.context(style_path):
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [1, 4, 9])
            assert ax.spines["top"].get_visible() is False
            assert ax.spines["right"].get_visible() is False
            plt.close(fig)
