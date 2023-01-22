from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def change_bar(theme: Theme):
    file: Path = Path.home() / "Projects/python/change-bar/config.py"
    new_file_content: str = apply_changes(
        content=file.read_text(),
        replacements=[(r"theme\=.*,", f'theme="{theme.name}",')],
    )

    update_file(file, new_file_content)
