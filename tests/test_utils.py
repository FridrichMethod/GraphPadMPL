"""Tests for mplplots.utils."""

import matplotlib.pyplot as plt

from mplplots.utils import auto_ticks


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
