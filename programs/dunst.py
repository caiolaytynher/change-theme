from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def dunst(theme: Theme):
    file: Path = Path.home() / ".config/dunst/dunstrc"
    new_file_content: str = apply_changes(
        content=file.read_text(),
        replacements=[
            (
                r"background\s=\s.* # primary background",
                f'background = "{theme.background}" # primary background',
            ),
            (
                r"foreground\s=\s.* # primary foreground",
                f'foreground = "{theme.foreground}" # primary foreground',
            ),
            (
                r"frame_color\s=\s.* # primary background light",
                f'frame_color = "{theme.contrast[0]}"'
                + " # primary background light",
            ),
            (
                r"background\s=\s.* # normal red",
                f'background = "{theme.alert}" # normal red',
            ),
            (
                r"frame_color\s=\s.* # bright red",
                f'frame_color = "{theme.alert}" # bright red',
            ),
        ],
    )

    update_file(file, new_file_content)

    Popen(["/usr/bin/killall", "dunst"])
