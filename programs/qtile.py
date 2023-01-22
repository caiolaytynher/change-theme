from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def qtile(theme: Theme):
    file: Path = Path.home() / ".config/qtile/themes/themes.py"
    new_file_content: str = apply_changes(
        content=file.read_text(),
        replacements=[
            (
                r"theme = .*",
                f"theme = {theme.name}",
            )
        ],
    )

    update_file(file, new_file_content)

    Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])
