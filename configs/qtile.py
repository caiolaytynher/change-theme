from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def qtile(theme: Theme):
    file_path: Path = Path.home() / ".config/qtile/themes/themes.py"
    file_content: str = get_file_content(file_path)
    new_file_content: str = apply_changes(
        content=file_content,
        replacements=[
            (
                r"theme = .*",
                f"theme = {theme.name}",
            )
        ],
    )

    update_file(file_path, new_file_content)

    Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])
