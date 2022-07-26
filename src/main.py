import os
import sys
import subprocess

import color_schemes
from color_scheme import ColorScheme
from helper_functions import change_line, change_lines, change_template

HOME = os.path.expanduser("~")
WALLPAPERS_PATH = "$HOME/Pictures/wallpapers"
VALID_COLOR_SCHEMES = {
    "gruvbox": color_schemes.gruvbox,
    "dracula": color_schemes.dracula,
}
COLOR_SCHEME_WALLPAPER = {
    "gruvbox": "serenity-1920x1080.jpg",
    "dracula": "blue-landscape.jpg",
}
COLOR_SCHEME_ACCENT_COLOR = {
    "gruvbox": "yellow",
    "dracula": "blue",
}


def main(args: list[str]) -> None:
    if len(args) > 1:
        color_scheme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    if color_scheme_name not in VALID_COLOR_SCHEMES:
        raise Exception("This coloscheme do not exist.")

    color_scheme: ColorScheme = VALID_COLOR_SCHEMES[color_scheme_name]

    # Change Wallpaper
    subprocess.Popen(
        [
            "/usr/bin/feh",
            "--bg-fill",
            f"{WALLPAPERS_PATH}/{COLOR_SCHEME_WALLPAPER[color_scheme_name]}",
        ]
    )
    change_line(
        filepath=f"{HOME}/.config/qtile/scripts/autostart.sh",
        target=r"feh\s--bg-fill\s\$HOME\/Pictures\/wallpapers\/.*",
        replacement=f"feh --bg-fill {WALLPAPERS_PATH}/{COLOR_SCHEME_WALLPAPER[color_scheme_name]}",
    )

    # Change Qtile
    change_line(
        filepath=f"{HOME}/.config/qtile/colors/__init__.py",
        target=r"colors:\sColorScheme\s=\scolor_schemes\..*",
        replacement=f"colors: ColorScheme = color_schemes.{color_scheme_name}",
    )
    change_line(
        filepath=f"{HOME}/.config/qtile/components/groups.py",
        target=r"colors\.normal\..*(?=,)",
        replacement=f"colors.normal.{COLOR_SCHEME_ACCENT_COLOR[color_scheme_name]}",
    )
    change_line(
        filepath=f"{HOME}/.config/qtile/components/panel.py",
        target=r"colors\.normal\..*(?=,)",
        replacement=f"colors.normal.{COLOR_SCHEME_ACCENT_COLOR[color_scheme_name]}",
    )
    subprocess.Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])

    # Change Alacritty
    change_line(
        filepath=f"{HOME}/.config/alacritty/alacritty.yml",
        target=r"colors:\s\*.*",
        replacement=f"colors: *{color_scheme_name}",
    )

    # Change Neovim
    change_line(
        filepath=f"{HOME}/.config/nvim/lua/caio/colorscheme.lua",
        target=r"local\scolorscheme\s=.*",
        replacement=f'local colorscheme = "{color_scheme_name}"',
    )
    change_line(
        filepath=f"{HOME}/.config/nvim/after/plugin/lualine.lua",
        target=r"theme\s=\s'.*'",
        replacement=f"theme = '{color_scheme_name}'",
    )

    # Change Rofi
    change_lines(
        filepath=f"{HOME}/.config/rofi/config.rasi",
        targets=[
            r"bg:\s.*;",
            r"bg-light:\s.*;",
            r"bg-lighter:\s.*;",
            r"fg:\s.*;",
            r"accent:\s.*;",
        ],
        replacements=[
            f"bg: {color_scheme.primary.background};",
            f"bg-light: {color_scheme.primary.background_light};",
            f"bg-lighter: {color_scheme.primary.background_lighter};",
            f"fg: {color_scheme.primary.foreground};",
            f"accent: {color_scheme.normal.__dict__[COLOR_SCHEME_ACCENT_COLOR[color_scheme_name]]};",
        ],
    )

    # Change Starship Prompt
    change_template(
        input_filepath=f"{HOME}/Documents/python/change-color-scheme/templates/starship.txt",
        targets=[
            r"background_lighter(?=[\s\)\"])",
            r"background_light(?=[\s\)\"])",
            r"background_dark(?=[\s\)\"])",
            r"background_darker(?=[\s\)\"])",
        ],
        replacements=[
            f"{color_scheme.primary.background_lighter}",
            f"{color_scheme.primary.background_light}",
            f"{color_scheme.primary.background_dark}",
            f"{color_scheme.primary.background_darker}",
        ],
        output_filepath=f"{HOME}/.config/starship.toml",
    )

    # Change dmenu
    change_lines(
        filepath=f"{HOME}/Documents/bash/custom-shell-scripts/custom-dmenu.sh",
        targets=[
            r"normal_background=.*",
            r"normal_foreground=.*",
            r"selected_background=.*",
            r"selected_foreground=.*",
        ],
        replacements=[
            f'normal_background="{color_scheme.primary.background}"',
            f'normal_foreground="{color_scheme.primary.foreground}"',
            f'selected_background="{color_scheme.normal.__dict__[COLOR_SCHEME_ACCENT_COLOR[color_scheme_name]]}"',
            f'selected_foreground="{color_scheme.primary.foreground}"',
        ],
    )

    # Change Dunst
    change_lines(
        filepath=f"{HOME}/.config/dunst/dunstrc",
        targets=[
            r"background\s=\s.* # primary background",
            r"foreground\s=\s.* # primary foreground",
            r"frame_color\s=\s.* # primary background light",
            r"background\s=\s.* # normal red",
            r"frame_color\s=\s.* # bright red",
        ],
        replacements=[
            f'background = "{color_scheme.primary.background}" # primary background',
            f'foreground = "{color_scheme.primary.foreground}" # primary foreground',
            f'frame_color = "{color_scheme.primary.background_light}" # primary background light',
            f'background = "{color_scheme.normal.red}" # normal red',
            f'frame_color = "{color_scheme.bright.red}" # bright red',
        ],
    )
    subprocess.Popen(["/usr/bin/killall", "dunst"])


if __name__ == "__main__":
    main(sys.argv)
