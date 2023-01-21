from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def neovim(theme: Theme):
    replacements = [
        (
            Path.home() / ".config/nvim/lua/caio/colorscheme.lua",
            [
                (
                    r"local\scolorscheme\s=.*",
                    f'local colorscheme = "{theme.name}"',
                )
            ],
        ),
        (
            Path.home() / ".config/nvim/after/plugin/lualine.lua",
            [(r'theme\s=\s".*"', f'theme = "{theme.name}"')],
        ),
    ]

    for file_path, replacement in replacements:
        file_content: str = get_file_content(file_path)
        new_file_content: str = apply_changes(
            content=file_content, replacements=replacement
        )

        update_file(file_path, new_file_content)
