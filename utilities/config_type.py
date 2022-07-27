from dataclasses import dataclass


@dataclass
class Config:
    command: list[str] | None
    input_paths: list[str]
    targets: list[str]
    replacements: list[str]
    output_paths: list[str] | None
