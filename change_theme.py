import sys

import themes
from programs import init_programs
from changes import apply_changes, ChangesToApply


def main(args: list[str]):
    if len(args) > 1:
        theme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    if theme_name not in themes.THEMES:
        raise Exception("This theme does not exist.")

    theme: themes.Theme = themes.THEMES[theme_name]
    programs: list[ChangesToApply] = init_programs(theme)

    for changes in programs:
        apply_changes(changes)


if __name__ == "__main__":
    main(sys.argv)
