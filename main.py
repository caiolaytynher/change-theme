import json
import os
import sys
import re
from typing import Pattern

HOME = os.path.expanduser("~")
PATH = f"{HOME}/Documents/python/change-colorscheme/colorschemes.json"


def read_color_data(filepath: str) -> dict[str]:
    with open(filepath, "r") as file:
        return json.load(file)


def change_line(
    filepath: str,
    target_regex: Pattern[str],
    replacement_text: str,
) -> None:
    with open(filepath, "r") as file:
        file_string = "".join(file.readlines())

    matches = target_regex.finditer(file_string)
    for match in matches:
        start, end = match.span()
        file_string = file_string.replace(file_string[start:end], replacement_text)

    with open(filepath, "w") as file:
        file.write(file_string)


def main(args: list[str]) -> None:
    if len(args) > 1:
        colorscheme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    colorscheme: dict[str] = read_color_data(PATH).get(colorscheme_name, {})
    if not colorscheme:
        raise Exception("This coloscheme do not exist.")

    change_line(
        f"{HOME}/.config/qtile/color_palletes.py",
        re.compile(r"colorscheme = data.get\(.*\)"),
        'colorscheme = data.get("monokai")',
    )


if __name__ == "__main__":
    # main(sys.argv)
    main(["python", "gruvbox"])
