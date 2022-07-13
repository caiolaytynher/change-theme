import json
import os

# from pprint import pprint


HOME = os.path.expanduser("~")
PATH = f"{HOME}/Documents/python/change-colorscheme/colorschemes.json"


def read_data(filepath: str) -> dict[str]:
    with open(filepath, "r") as file:
        return json.load(file)


def main() -> None:
    data: dict[str] = read_data(PATH)


if __name__ == "__main__":
    main()
