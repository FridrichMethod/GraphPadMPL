"""Tests for mplplots.utils."""

from pathlib import Path

import matplotlib.pyplot as plt

from mplplots.utils import auto_ticks, norm_path


class TestNormPath:
    def test_resolves_relative_path(self) -> None:
        result = norm_path(".")
        assert result.is_absolute()
        assert result.exists()

    def test_expanduser(self) -> None:
        result = norm_path("~", resolve=False)
        assert "~" not in str(result)

    def test_with_path_object(self) -> None:
        result = norm_path(Path("."))
        assert isinstance(result, Path)
        assert result.is_absolute()

    def test_resolve_false(self) -> None:
        result = norm_path(".", resolve=False)
        assert not result.is_absolute()


class TestAutoTicks:
    def test_sets_ticks_on_simple_plot(self) -> None:
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        auto_ticks(ax)
        assert len(ax.get_xticks()) >= 3
        assert len(ax.get_yticks()) >= 3
        plt.close(fig)

    def test_respects_explicit_limits(self) -> None:
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        auto_ticks(ax, left=0.5, right=3.5, bottom=0, top=10)
        assert ax.get_xlim()[0] == 0.5
        assert ax.get_xlim()[1] == 3.5
        assert ax.get_ylim()[0] == 0
        assert ax.get_ylim()[1] == 10
        plt.close(fig)
