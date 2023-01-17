from pathlib import Path
from subprocess import Popen

from themes.theme import Theme
from handlers.files import update_file, get_file_content, apply_changes


def wallpaper(theme: Theme):
    file_path: Path = Path.home() / ".config/qtile/scripts/autostart.sh"
    file_content: str = get_file_content(file_path)
    new_file_content: str = apply_changes(
        content=file_content,
        replacements=[
            (
                r"feh\s--bg-fill\s\$HOME\/Pictures\/wallpapers\/.*",
                f"feh --bg-fill $HOME/Pictures/wallpapers/{theme.wallpaper}",
            )
        ],
    )

    update_file(file_path, new_file_content)

    Popen(
        [
            "/usr/bin/feh",
            "--bg-fill",
            Path.home() / f"Pictures/wallpapers/{theme.wallpaper}",
        ]
    )
