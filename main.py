import sys

from themes import themes
from themes.theme import Theme
from programs.wallpaper import wallpaper
from programs.qtile import qtile
from programs.alacritty import alacritty
from programs.neovim import neovim
from programs.rofi import rofi
from programs.starship import starship
from programs.dmenu import dmenu
from programs.dunst import dunst

VALID_THEMES = {
    "gruvbox": themes.gruvbox,
    "dracula": themes.dracula,
    "catppuccin": themes.catppuccin,
    "tokyonight": themes.tokyonight,
    "everforest": themes.everforest,
    "kanagawa": themes.kanagawa,
    "onedark": themes.onedark,
}


def main(args: list[str]):
    if len(args) > 1:
        theme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    if theme_name not in VALID_THEMES:
        raise Exception("This theme does not exist.")

    theme: Theme = VALID_THEMES[theme_name]

    programs = [
        wallpaper,
        qtile,
        alacritty,
        neovim,
        rofi,
        starship,
        dmenu,
        dunst,
    ]

    for program in programs:
        program(theme)


if __name__ == "__main__":
    main(sys.argv)
