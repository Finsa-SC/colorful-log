class ColorsMeta(type):
    def __getattribute__(cls, name: str):
        if not name.startswith("_"):
            custom = type.__getattribute__(cls, "_custom_colors")
            if name in custom:
                return custom[name]

        try:
            return type.__getattribute__(cls, name)
        except AttributeError as e:
            raise AttributeError(
                f"Colors has no attribute {name!r}"
            ) from e

class Colors(metaclass=ColorsMeta):
    _custom_colors: dict[str, str] = {}
    _reserved = {"RESET", "register"}

    @classmethod
    def register(cls, name: str, value: str):
        if name in cls._reserved or name.startswith("_"):
            raise ValueError(f"{name!r} is reserved and cannot be registered")

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