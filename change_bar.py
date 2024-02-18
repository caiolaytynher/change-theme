import sys

from programs import init_programs
from changes import apply_changes, ChangesToApply

BARS = ["normal", "vibrant", "utility"]


def main(args: list[str]):
    if len(args) > 1:
        bar: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    if bar not in BARS:
        raise Exception(f"{bar!r} is not a valid bar.")

    theme: themes.Theme = themes.THEMES[theme_name]
    programs: list[ChangesToApply] = init_programs(theme)

    for changes in programs:
        apply_changes(changes)


if __name__ == "__main__":
    main(sys.argv)
