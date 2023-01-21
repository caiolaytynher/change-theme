from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def dmenu(theme: Theme):
    file_path: Path = (
        Path.home() / "Projects/bash/custom-shell-scripts/custom-dmenu.sh"
    )
    file_content: str = get_file_content(file_path)
    new_file_content: str = apply_changes(
        content=file_content,
        replacements=[
            (
                r"normal_background=.*",
                f'normal_background="{theme.background}"',
            ),
            (
                r"normal_foreground=.*",
                f'normal_foreground="{theme.foreground}"',
            ),
            (
                r"selected_background=.*",
                f'selected_background="{theme.accent}"',
            ),
            (
                r"selected_foreground=.*",
                f'selected_foreground="{theme.foreground}"',
            ),
        ],
    )

    update_file(file_path, new_file_content)
