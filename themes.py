from pathlib import Path
from dataclasses import dataclass


@dataclass
class Theme:
    name: str
    background: str
    contrast: list[str]  # higher index -> lighter color
    foreground: str
    wallpaper: Path
    accent: str
    alert: str


THEMES: dict[str, Theme] = {
    "gruvbox": Theme(
        name="gruvbox",
        background="#282828",
        contrast=[
            "#3c3836",
            "#504945",
            "#665c54",
            "#7c6f64",
        ],
        foreground="#ebdbb2",
        wallpaper=Path.home()
        / "Themes/Gruvbox-GTK-Theme/wallpapers/gruvbox20.png",
        accent="#d65d0e",  # Orange
        alert="#cc241d",
    ),
    "dracula": Theme(
        name="dracula",
        background="#282a36",
        contrast=[
            "#343746",
            "#424450",
            "#535560",
            "#63646e",
        ],
        foreground="#f8f8f2",
        wallpaper=Path.home()
        / "Themes/Dracula-wallpapers/first-collection/dracula-wallpaper.svg",
        accent="#bd93f9",  # Blue
        alert="#ff5555",
    ),
    "catppuccin": Theme(
        name="catppuccin",
        background="#1E1E2E",
        contrast=[
            "#343547",
            "#3F4154",
            "#4A4C60",
            "#767A91",
        ],
        wallpaper=Path.home()
        / "Themes/Catppuccin-wallpapers/mandelbrot/mandelbrot_full_flamingo.png",
        foreground="#CDD6F4",
        accent="#F5C2E7",  # Pink
        alert="#F38BA8",
    ),
    "tokyonight": Theme(
        name="tokyonight",
        background="#24283b",
        contrast=[
            "#2E3347",
            "#383D53",
            "#4B516A",
            "#727998",
        ],
        wallpaper=Path.home()
        / "Themes/Tokyo-Night-GTK-Theme/wallpapers/tokyo-night31.png",
        foreground="#c0caf5",
        accent="#f7768e",  # Red
        alert="#f7768e",
    ),
    "everforest": Theme(
        name="everforest",
        background="#2d353b",
        contrast=[
            "#383F42",
            "#424849",
            "#575A57",
            "#807E73",
        ],
        wallpaper=Path.home()
        / "Themes/Everforest-GTK-Theme/wallpapers/everforest01.jpg",
        foreground="#d3c6aa",
        accent="#a7c080",  # Green
        alert="#e67e80",
    ),
    "kanagawa": Theme(
        name="kanagawa",
        background="#1f1f28",
        contrast=[
            "#2B2B32",
            "#37363B",
            "#4F4D4D",
            "#7E7B71",
        ],
        wallpaper=Path.cwd()
        / "Pictures/wallpapers/the-great-wave-minimal.png",
        foreground="#dcd7ba",
        accent="#7e9cd8",  # Blue
        alert="#c34043",
    ),
    "onedark": Theme(
        name="onedark",
        background="#1e2127",
        contrast=[
            "#272B31",
            "#30343A",
            "#42464D",
            "#656A73",
        ],
        wallpaper=Path.cwd() / "Themes/OneDarkWallpapers/34.png",
        foreground="#abb2bf",
        accent="#e06c75",  # Red
        alert="#e06c75",
    ),
}
