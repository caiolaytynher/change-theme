from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, apply_changes


def starship(theme: Theme):
    template: Path = (
        Path.home() / "Projects/python/change-theme/templates/starship.toml"
    )
    file: Path = Path.home() / ".config/starship.toml"
    new_file_content: str = apply_changes(
        content=template.read_text(),
        replacements=[
            (
                r"contrast0(?=[\s\)\"])",
                f"{theme.contrast[0]}",
            ),
            (
                r"contrast1(?=[\s\)\"])",
                f"{theme.contrast[1]}",
            ),
            (
                r"contrast2(?=[\s\)\"])",
                f"{theme.contrast[2]}",
            ),
            (
                r"contrast3(?=[\s\)\"])",
                f"{theme.contrast[3]}",
            ),
        ],
    )

    update_file(file, new_file_content)
