import json
import os
import sys

from pprint import pprint


HOME = os.path.expanduser("~")
PATH = f"{HOME}/Documents/python/change-colorscheme/colorschemes.json"


def read_color_data(filepath: str) -> dict[str]:
    with open(filepath, "r") as file:
        return json.load(file)


def change_line(filepath: str, targeted_text: str, replacement_text: str) -> None:
    with open(filepath, "r") as file:
        file_content = file.readlines()

    for i, line in enumerate(file_content):
        if targeted_text in line:
            file_content[i] = line.replace(targeted_text, replacement_text)

    with open(filepath, "w") as file:
        for line in file_content:
            file.write(line)


def main(args: list[str]) -> None:
    if len(args) > 1:
        colorscheme_name: str = args[1]
    else:
        raise Exception("You must provide one argument.")

    colorscheme: dict[str] = read_color_data(PATH).get(colorscheme_name, {})
    if not colorscheme:
        raise Exception("This coloscheme do not exist.")

    change_line("./testfile.txt", "blue", "yellow")


if __name__ == "__main__":
    # main(sys.argv)
    main(["python", "gruvbox"])
