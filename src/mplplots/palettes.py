"""Color palettes for mplplots."""

from itertools import cycle

# Raw color list for indexing/slicing; use cycle() for iterator usage
CUSTOM: tuple[str, ...] = (
    "#BCE4F9",
    "#7BD3F2",
    "#F0AECB",
    "#E88791",
    "#C4DDB1",
    "#97D9A8",
    "#CCCCE6",
    "#9D9DCF",
    "#8FB0DD",
    "#F0CEA4",
    "#F8A450",
)
CUSTOM_CYCLE = cycle(CUSTOM)
