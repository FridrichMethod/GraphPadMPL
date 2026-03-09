"""Utility functions for mplplots."""

import os
from pathlib import Path

import matplotlib.font_manager as fm
from matplotlib import ticker
from matplotlib.axes import Axes

type StrPath = str | os.PathLike[str]


def norm_path(
    path: StrPath,
    expandvars: bool = True,
    expanduser: bool = True,
    resolve: bool = True,
) -> Path:
    """Normalize a file path.

    Args:
        path (StrPath): The file path to normalize.
        expandvars (bool, optional): Whether to expand environment variables. Defaults to True.
        expanduser (bool, optional): Whether to expand the user directory. Defaults to True.
        resolve (bool, optional): Whether to resolve the path. Defaults to True.

    Returns:
        The normalized file path.
    """
    p = Path(path)
    if expandvars:
        p = Path(os.path.expandvars(p))
    if expanduser:
        p = p.expanduser()
    if resolve:
        p = p.resolve()

    return p


def add_custom_fonts(*paths: StrPath) -> None:
    """Add custom fonts to the font manager.

    Args:
        paths (StrPath): Paths to font files to register.
    """
    for path in paths:
        fm.fontManager.addfont(path)


def auto_ticks(  # noqa: C901
    ax: Axes,
    *,
    left: float | None = None,
    right: float | None = None,
    bottom: float | None = None,
    top: float | None = None,
) -> None:
    """Set the major and minor ticks of an axis automatically.

    Args:
        ax (Axes): The axis to set ticks for.
        left (float | None, optional): The left limit of the x-axis. Defaults to None.
        right (float | None, optional): The right limit of the x-axis. Defaults to None.
        bottom (float | None, optional): The bottom limit of the y-axis. Defaults to None.
        top (float | None, optional): The top limit of the y-axis. Defaults to None.

    Notes:
        Put this function after the data are passed to the axis.
    """
    # Set the major and minor ticks of the x-axis
    if left is not None:
        ax.set_xlim(left=left)
    if right is not None:
        ax.set_xlim(right=right)

    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=3))
    x_tick_num = len(ax.get_xticks())
    if x_tick_num >= 6:
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    elif x_tick_num >= 5:
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    else:
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))

    # For viewing incomplete ticks
    if left is None and (ax.get_xticks()[0] != ax.get_xlim()[0]):
        ax.set_xlim(left=ax.get_xticks()[0])
    if right is None and (ax.get_xticks()[-1] != ax.get_xlim()[-1]):
        ax.set_xlim(right=ax.get_xticks()[-1])

    # Set the major and minor ticks of the y-axis
    if bottom is not None:
        ax.set_ylim(bottom=bottom)
    if top is not None:
        ax.set_ylim(top=top)

    ax.yaxis.set_major_locator(ticker.MaxNLocator(nbins=6, min_n_ticks=3))
    y_tick_num = len(ax.get_yticks())
    if y_tick_num >= 6:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    elif y_tick_num >= 5:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    else:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))

    # For viewing incomplete ticks
    if bottom is None and (ax.get_yticks()[0] != ax.get_ylim()[0]):
        ax.set_ylim(bottom=ax.get_yticks()[0])
    if top is None and (ax.get_yticks()[-1] != ax.get_ylim()[-1]):
        ax.set_ylim(top=ax.get_yticks()[-1])
