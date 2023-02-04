from pathlib import Path

from themes import Theme
from changes import ChangesToApply


def init_programs(theme: Theme) -> list[ChangesToApply]:
    return [
        # Alacritty
        ChangesToApply(
            file=Path.home() / ".config/alacritty/alacritty.yml",
            replacements=[(r"colors:\s\*.*", f"colors: *{theme.name}")],
        ),
        # Change bar
        ChangesToApply(
            file=Path.home() / "Projects/python/change-bar/config.py",
            replacements=[(r"theme\=.*,", f'theme="{theme.name}",')],
        ),
        # Dmenu
        ChangesToApply(
            file=Path.home()
            / "Projects/bash/custom-shell-scripts/custom-dmenu.sh",
            replacements=[
                (
                    r"normal_background=.*",
                    f'normal_background="{theme.background}"',
                ),
                (
                    r"normal_foreground=.*",
                    f'normal_foreground="{theme.foreground}"',
                ),
                (
                    r"selected_background=.*",
                    f'selected_background="{theme.accent}"',
                ),
                (
                    r"selected_foreground=.*",
                    f'selected_foreground="{theme.foreground}"',
                ),
            ],
        ),
        # Dunst
        ChangesToApply(
            file=Path.home() / ".config/dunst/dunstrc",
            replacements=[
                (
                    r"background\s=\s.* # primary background",
                    f'background = "{theme.background}" # primary background',
                ),
                (
                    r"foreground\s=\s.* # primary foreground",
                    f'foreground = "{theme.foreground}" # primary foreground',
                ),
                (
                    r"frame_color\s=\s.* # primary background light",
                    f'frame_color = "{theme.contrast[0]}"'
                    + " # primary background light",
                ),
                (
                    r"background\s=\s.* # normal red",
                    f'background = "{theme.alert}" # normal red',
                ),
                (
                    r"frame_color\s=\s.* # bright red",
                    f'frame_color = "{theme.alert}" # bright red',
                ),
            ],
            command=["/usr/bin/killall", "dunst"],
        ),
        # Neovim
        ChangesToApply(
            file=Path.home() / ".config/nvim/lua/caio/colorscheme.lua",
            replacements=[
                (
                    r"local\scolorscheme\s=.*",
                    f'local colorscheme = "{theme.name}"',
                )
            ],
        ),
        ChangesToApply(
            file=Path.home() / ".config/nvim/after/plugin/lualine.lua",
            replacements=[(r'theme\s=\s".*"', f'theme = "{theme.name}"')],
        ),
        # Qtile
        ChangesToApply(
            file=Path.home() / ".config/qtile/themes/themes.py",
            replacements=[
                (
                    r"theme = .*",
                    f"theme = {theme.name}",
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
        # Rofi
        ChangesToApply(
            file=Path.home() / ".config/rofi/config.rasi",
            replacements=[
                (
                    r"bg:\s.*;",
                    f"bg: {theme.background};",
                ),
                (
                    r"bg-light:\s.*;",
                    f"bg-light: {theme.contrast[0]};",
                ),
                (
                    r"bg-lighter:\s.*;",
                    f"bg-lighter: {theme.contrast[1]};",
                ),
                (
                    r"fg:\s.*;",
                    f"fg: {theme.foreground};",
                ),
                (
                    r"accent:\s.*;",
                    f"accent: {theme.accent};",
                ),
            ],
        ),
        # Starship
        ChangesToApply(
            template=Path.home()
            / "Projects/python/change-theme/templates/starship.toml",
            file=Path.home() / ".config/starship.toml",
            replacements=[
                (
                    r"contrast0(?=[\s\)\"])",
                    f"{theme.contrast[0]}",
                ),
                (
                    r"contrast1(?=[\s\)\"])",
                    f"{theme.contrast[1]}",
                ),
                (
                    r"contrast2(?=[\s\)\"])",
                    f"{theme.contrast[2]}",
                ),
                (
                    r"contrast3(?=[\s\)\"])",
                    f"{theme.contrast[3]}",
                ),
            ],
        ),
        # Wallpaper
        ChangesToApply(
            file=Path.home() / ".config/qtile/scripts/autostart.sh",
            replacements=[
                (
                    r"feh\s--bg-fill\s.*",
                    f"feh --bg-fill {theme.wallpaper}",
                )
            ],
            command=["/usr/bin/feh", "--bg-fill", theme.wallpaper],
        ),
    ]
