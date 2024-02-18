from pathlib import Path

from changes import ChangesToApply
from bar_assets import BarAssets


def init_bars(bar: str, assets: BarAssets) -> list[ChangesToApply]:
    return [
        # Qtile
        ChangesToApply(
            file=Path.home() / ".config/qtile/config.py",
            replacements=[
                (
                    r"components\.panels\..*\simport",
                    f"components.panels.{bar} import",
                )
            ],
        ),
        ChangesToApply(
            file=Path.home() / ".config/qtile/components/groups.py",
            replacements=[
                (
                    r"\"border_focus\":\stheme\..*,",
                    '"border_focus": theme.accent,'
                    if bar == "vibrant"
                    else '"border_focus": theme.contrast[3],',
                )
            ],
        ),
        ChangesToApply(
            file=Path.home() / ".config/qtile/scripts/autostart.sh",
            replacements=[
                (
                    r"feh\s--bg-fill\s.*",
                    f"feh --bg-fill {assets.wallpapers[assets.theme][bar]}",
                )
            ],
            command=[
                "/usr/bin/qtile",
                "cmd-obj",
                "-o",
                "cmd",
                "-f",
                "restart",
            ],
        ),
        # Picom
        ChangesToApply(
            file=Path.home() / ".config/picom/picom.conf",
            replacements=[
                (
                    r"corner-radius\s=\s.*;",
                    "corner-radius = 0;"
                    if bar == "utility"
                    else "corner-radius = 10;",
                )
            ],
            # Wallpaper
            # Is inside Picom for convenience.
            command=[
                "/usr/bin/feh",
                "--bg-fill",
                assets.wallpapers[assets.theme][bar],
            ],
        ),
    ]
