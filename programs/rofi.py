from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def rofi(theme: Theme):
    file: Path = Path.home() / ".config/rofi/config.rasi"
    new_file_content: str = apply_changes(
        content=file.read_text(),
        replacements=[
            (
                r"bg:\s.*;",
                f"bg: {theme.background};",
            ),
            (
                r"bg-light:\s.*;",
                f"bg-light: {theme.contrast[0]};",
            ),
            (
                r"bg-lighter:\s.*;",
                f"bg-lighter: {theme.contrast[1]};",
            ),
            (
                r"fg:\s.*;",
                f"fg: {theme.foreground};",
            ),
            (
                r"accent:\s.*;",
                f"accent: {theme.accent};",
            ),
        ],
    )

    update_file(file, new_file_content)
