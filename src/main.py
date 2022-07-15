import os
import sys
import re

import color_schemes
from color_scheme import ColorScheme
from helper_functions import change_line

HOME = os.path.expanduser("~")
VALID_COLORSCHEMES = {
    "gruvbox": color_schemes.gruvbox,
    "dracula": color_schemes.dracula,
}


def main(args: list[str]) -> None:
    if len(args) > 1:
        colorscheme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    colorscheme: ColorScheme = ).get(colorscheme_name, {})
    if not colorscheme:
        raise Exception("This coloscheme do not exist.")

    # Change Qtile
    change_line(
        filepath=f"{HOME}/.config/qtile/color_palletes.py",
        target_regex=re.compile(r"colorscheme = data.get\(.*\)"),
        replacement_text=f'colorscheme = data.get("{colorscheme_name}")',
    )

    # Change Alacritty
    change_line(
        filepath=f"{HOME}/.config/alacritty/alacritty.yml",
        target_regex=re.compile(r"colors: \*.*"),
        replacement_text=f"colors: *{colorscheme_name}",
    )

    # Change Neovim
    translate_name = {
        "GarudaDracula": "dracula",
        "GruvboxDark": "gruvbox",
    }
    change_line(
        filepath=f"{HOME}/.config/nvim/init.vim",
        target_regex=re.compile(r"colorscheme .*"),
        replacement_text=f"colorscheme {translate_name[colorscheme_name]}",
    )
    change_line(
        filepath=f"{HOME}/.config/nvim/after/plugin/lualine.rc.lua",
        target_regex=re.compile(r"theme = '.*'"),
        replacement_text=f"theme = '{translate_name[colorscheme_name]}'",
    )

    # Change Rofi
    change_line(
        filepath=f"{HOME}/.config/rofi/config.rasi",
        target_regex=re.compile(r"bg: .*;"),
        replacement_text=f"bg: {colorscheme['primary']['background']};",
    )
    change_line(
        filepath=f"{HOME}/.config/rofi/config.rasi",
        target_regex=re.compile(r"fg: .*;"),
        replacement_text=f"fg: {colorscheme['primary']['foreground']};",
    )
    for color_name, color_hex in colorscheme["normal"].items():
        change_line(
            filepath=f"{HOME}/.config/rofi/config.rasi",
            target_regex=re.compile(rf"{color_name}: .*;"),
            replacement_text=f"{color_name}: {color_hex};",
        )


if __name__ == "__main__":
    # main(sys.argv)
    main(["python", "gruvbox"])
