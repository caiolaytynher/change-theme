import sys

import themes
from programs import init_programs, ProgramsType
from update_files import apply_changes

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

    theme: themes.Theme = VALID_THEMES[theme_name]
    programs: ProgramsType = init_programs(theme)

    # Type ignored from this point because LSP can't tell that it is
    # indeed the right types.
    for _, params in programs.items():
        if isinstance(params, list):
            for param in params:
                apply_changes(**param)  # type: ignore
        else:
            apply_changes(**params)  # type: ignore


if __name__ == "__main__":
    main(sys.argv)
