import sys

from themes import themes
from themes.theme import Theme
from configs.wallpaper import wallpaper
from configs.qtile import qtile
from configs.alacritty import alacritty
from configs.neovim import neovim
from configs.rofi import rofi
from configs.starship import starship
from configs.dmenu import dmenu
from configs.dunst import dunst

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

    configs = [
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
        config(theme)


if __name__ == "__main__":
    main(sys.argv)
