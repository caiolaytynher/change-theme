from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def alacritty(theme: Theme):
    file: Path = Path.home() / ".config/alacritty/alacritty.yml"
    new_file_content: str = apply_changes(
        content=file.read_text(),
        replacements=[(r"colors:\s\*.*", f"colors: *{theme.name}")],
    )

    update_file(file, new_file_content)
