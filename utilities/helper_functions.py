def get_file_str(filepath: str) -> str:
    with open(filepath, "r") as file:
        return "".join(file.readlines())


def update_file(filepath: str, content: str) -> None:
    with open(filepath, "w") as file:
        file.write(content)
