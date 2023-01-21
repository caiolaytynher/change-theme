from dataclasses import dataclass
from pathlib import Path


@dataclass
class Theme:
    name: str
    background: str
    contrast: list[str]  # higher index -> lighter color
    foreground: str
    wallpaper: Path
    accent: str
    alert: str
