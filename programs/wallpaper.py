from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def wallpaper(theme: Theme):
    file: Path = Path.home() / ".config/qtile/scripts/autostart.sh"
    new_file_content: str = apply_changes(
        content=file.read_text(),
        replacements=[
            (
                r"feh\s--bg-fill\s.*",
                f"feh --bg-fill {theme.wallpaper}",
            )
        ],
    )

    update_file(file, new_file_content)

    Popen(["/usr/bin/feh", "--bg-fill", theme.wallpaper])
