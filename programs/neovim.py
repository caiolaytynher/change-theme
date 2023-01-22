from pathlib import Path

from themes.theme import Theme
from handlers.files import update_file, apply_changes


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

    for file, replacement in replacements:
        new_file_content: str = apply_changes(
            content=file.read_text(), replacements=replacement
        )

        update_file(file, new_file_content)
