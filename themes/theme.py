from dataclasses import dataclass


@dataclass
class Theme:
    name: str
    background: str
    contrast: list[str]  # higher index -> lighter color
    foreground: str
    wallpaper: str
    accent: str
    alert: str
