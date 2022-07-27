import os
import re
import sys
import subprocess
from typing import Pattern

from colors import color_schemes
from colors.color_scheme import ColorScheme
from utilities.helper_functions import get_file_str, update_file
from utilities.config_type import Config

HOME = os.path.expanduser("~")
VALID_COLORS = {
    "gruvbox": color_schemes.gruvbox,
    "dracula": color_schemes.dracula,
}


def main(args: list[str]) -> None:
    if len(args) > 1:
        color_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    if color_name not in VALID_COLORS:
        raise Exception("This color scheme does not exist.")

    colors: ColorScheme = VALID_COLORS[color_name]
    accent: str = colors.normal.__dict__[colors.accent]

    wallpaper = Config(
        command=[
            "/usr/bin/feh",
            "--bg-fill",
            f"{HOME}/Pictures/wallpapers/{colors.wallpaper}",
        ],
        input_paths=[f"{HOME}/.config/qtile/scripts/autostart.sh"],
        targets=[r"feh\s--bg-fill\s\$HOME\/Pictures\/wallpapers\/.*"],
        replacements=[f"feh --bg-fill $HOME/Pictures/wallpapers/{colors.wallpaper}"],
        output_paths=None,
    )

    qtile = Config(
        command=["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"],
        input_paths=[
            f"{HOME}/.config/qtile/colors/__init__.py",
            f"{HOME}/.config/qtile/components/groups.py",
            f"{HOME}/.config/qtile/components/panel.py",
        ],
        targets=[
            r"colors:\sColorScheme\s=\scolor_schemes\..*",
            r"colors\.normal\..*(?=,)",
            r"colors\.normal\..*(?=,)",
        ],
        replacements=[
            f"colors: ColorScheme = color_schemes.{color_name}",
            f"colors.normal.{colors.accent}",
            f"colors.normal.{colors.accent}",
        ],
        output_paths=None,
    )

    alacritty = Config(
        command=None,
        input_paths=[f"{HOME}/.config/alacritty/alacritty.yml"],
        targets=[r"colors:\s\*.*"],
        replacements=[f"colors: *{color_name}"],
        output_paths=None,
    )

    neovim = Config(
        command=None,
        input_paths=[
            f"{HOME}/.config/nvim/lua/caio/colorscheme.lua",
            f"{HOME}/.config/nvim/after/plugin/lualine.lua",
        ],
        targets=[
            r"local\scolorscheme\s=.*",
            r"theme\s=\s'.*'",
        ],
        replacements=[
            f'local colorscheme = "{color_name}"',
            f"theme = '{color_name}'",
        ],
        output_paths=None,
    )

    rofi = Config(
        command=None,
        input_paths=[f"{HOME}/.config/rofi/config.rasi"],
        targets=[
            r"bg:\s.*;",
            r"bg-light:\s.*;",
            r"bg-lighter:\s.*;",
            r"fg:\s.*;",
            r"accent:\s.*;",
        ],
        replacements=[
            f"bg: {colors.primary.background};",
            f"bg-light: {colors.primary.contrast[0]};",
            f"bg-lighter: {colors.primary.contrast[1]};",
            f"fg: {colors.primary.foreground};",
            f"accent: {accent};",
        ],
        output_paths=None,
    )

    starship = Config(
        command=None,
        input_paths=[
            f"{HOME}/Documents/python/change-color-scheme/templates/starship.toml"
        ],
        targets=[
            r"contrast0(?=[\s\)\"])",
            r"contrast1(?=[\s\)\"])",
            r"contrast2(?=[\s\)\"])",
            r"contrast3(?=[\s\)\"])",
        ],
        replacements=[
            f"{colors.primary.contrast[0]}",
            f"{colors.primary.contrast[1]}",
            f"{colors.primary.contrast[2]}",
            f"{colors.primary.contrast[3]}",
        ],
        output_paths=[f"{HOME}/.config/starship.toml"],
    )

    dmenu = Config(
        command=None,
        input_paths=[f"{HOME}/Documents/bash/custom-shell-scripts/custom-dmenu.sh"],
        targets=[
            r"normal_background=.*",
            r"normal_foreground=.*",
            r"selected_background=.*",
            r"selected_foreground=.*",
        ],
        replacements=[
            f'normal_background="{colors.primary.background}"',
            f'normal_foreground="{colors.primary.foreground}"',
            f'selected_background="{accent}"',
            f'selected_foreground="{colors.primary.foreground}"',
        ],
        output_paths=None,
    )

    dunst = Config(
        command=["/usr/bin/killall", "dunst"],
        input_paths=[f"{HOME}/.config/dunst/dunstrc"],
        targets=[
            r"background\s=\s.* # primary background",
            r"foreground\s=\s.* # primary foreground",
            r"frame_color\s=\s.* # primary background light",
            r"background\s=\s.* # normal red",
            r"frame_color\s=\s.* # bright red",
        ],
        replacements=[
            f'background = "{colors.primary.background}" # primary background',
            f'foreground = "{colors.primary.foreground}" # primary foreground',
            f'frame_color = "{colors.primary.contrast[0]}" # primary background light',
            f'background = "{colors.normal.red}" # normal red',
            f'frame_color = "{colors.bright.red}" # bright red',
        ],
        output_paths=None,
    )

    # TODO: Allow for multiple targets on multiple files
    configs: list[Config] = [
        wallpaper,
        qtile,
        alacritty,
        neovim,
        rofi,
        starship,
        dmenu,
        dunst,
    ]

    for config in configs:
        if len(config.input_paths) > 1:
            for i, (input_path, target, replacement) in enumerate(
                zip(
                    config.input_paths,
                    config.targets,
                    config.replacements,
                )
            ):
                file_content: str = get_file_str(input_path)
                pattern: Pattern[str] = re.compile(target)
                mod_file_content: str = pattern.sub(replacement, file_content)

                output_path: str = (
                    config.output_paths[i]
                    if config.output_paths is not None
                    else input_path
                )
                update_file(output_path, mod_file_content)
        else:
            input_path: str = config.input_paths[0]
            file_content: str = get_file_str(input_path)

            mod_file_content = file_content
            for target, replacement in zip(config.targets, config.replacements):
                pattern: Pattern[str] = re.compile(target)
                mod_file_content: str = pattern.sub(replacement, mod_file_content)

            output_path: str = (
                config.output_paths[0]
                if config.output_paths is not None
                else input_path
            )
            update_file(output_path, mod_file_content)

        if config.command is not None:
            subprocess.Popen(config.command)


if __name__ == "__main__":
    main(sys.argv)
