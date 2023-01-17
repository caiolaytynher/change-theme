from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def starship(theme: Theme):
    template: Path = (
        Path.home() / "Projects/change-theme/templates/starship.toml"
    )
    file_path: Path = Path.home() / ".config/starship.toml"
    file_content: str = get_file_content(template)
    new_file_content: str = apply_changes(
        content=file_content,
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

    update_file(file_path, new_file_content)
