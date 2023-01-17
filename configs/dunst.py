from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def dunst(theme: Theme):
    file_path: Path = Path.home() / ".config/dunst/dunstrc"
    file_content: str = get_file_content(file_path)
    new_file_content: str = apply_changes(
        content=file_content,
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
                f'background = "{theme.accent}" # normal red',
            ),
            (
                r"frame_color\s=\s.* # bright red",
                f'frame_color = "{theme.accent}" # bright red',
            ),
        ],
    )

    update_file(file_path, new_file_content)

    Popen(["/usr/bin/killall", "dunst"])
