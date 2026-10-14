class ColorsMeta(type):
    def __getattr__(cls, name: str):
        try:
            return cls._custom_colors[name]
        except KeyError as e:
            raise AttributeError(
                f"Colors has no attribute {name!r}"
            ) from e

class Colors(metaclass=ColorsMeta):
    _custom_colors: dict[str, str] = {}

    @classmethod
    def register(cls, name: str, value: str):
        cls._custom_colors[name] = value

    BLACK = "0"
    RED = "1"
    GREEN = "2"
    YELLOW = "3"
    BLUE = "4"
    MAGENTA = "5"
    CYAN = "6"
    WHITE = "7"
    RESET = "9"