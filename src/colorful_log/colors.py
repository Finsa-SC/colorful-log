from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    BLACK = "0"
    RED = "1"
    GREEN = "2"
    YELLOW = "3"
    BLUE = "4"
    MAGENTA = "5"
    CYAN = "6"
    WHITE = "7"
    RESET = "\033[0m"