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
        color_scheme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    if color_scheme_name not in VALID_COLORSCHEMES:
        raise Exception("This coloscheme do not exist.")

    color_scheme: ColorScheme = VALID_COLORSCHEMES[color_scheme_name]

    # Change Qtile
    change_line(
        filepath=f"{HOME}/.config/qtile/config.py",
        target_regex=re.compile(r"colors = color_schemes\..*"),
        replacement_text=f"colors = color_schemes.{color_scheme_name}",
    )

    # Change Alacritty
    change_line(
        filepath=f"{HOME}/.config/alacritty/alacritty.yml",
        target_regex=re.compile(r"colors: \*.*"),
        replacement_text=f"colors: *{color_scheme_name}",
    )

    # Change Neovim
    change_line(
        filepath=f"{HOME}/.config/nvim/init.vim",
        target_regex=re.compile(r"colorscheme .*"),
        replacement_text=f"colorscheme {color_scheme_name}",
    )
    change_line(
        filepath=f"{HOME}/.config/nvim/after/plugin/lualine.rc.lua",
        target_regex=re.compile(r"theme = '.*'"),
        replacement_text=f"theme = '{color_scheme_name}'",
    )

    # Change Rofi
    change_line(
        filepath=f"{HOME}/.config/rofi/config.rasi",
        target_regex=re.compile(r"bg: .*;"),
        replacement_text=f"bg: {color_scheme.primary.background};",
    )
    change_line(
        filepath=f"{HOME}/.config/rofi/config.rasi",
        target_regex=re.compile(r"fg: .*;"),
        replacement_text=f"fg: {color_scheme.primary.foreground};",
    )
    change_line(
        filepath=f"{HOME}/.config/rofi/config.rasi",
        target_regex=re.compile(r"accent: .*;"),
        replacement_text=f"accent: {color_scheme.normal.yellow};",
    )


if __name__ == "__main__":
    main(sys.argv)
