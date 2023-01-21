from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def alacritty(theme: Theme):
    file_path: Path = Path.home() / ".config/alacritty/alacritty.yml"
    file_content: str = get_file_content(file_path)
    new_file_content: str = apply_changes(
        content=file_content,
        replacements=[(r"colors:\s\*.*", f"colors: *{theme.name}")],
    )

    update_file(file_path, new_file_content)
