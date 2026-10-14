from colorful_log.engine import PrintLogEngine
from colorful_log.colors import Colors
from colorful_log.styles import StylesAPI
from copy import copy

class PrintLog(PrintLogEngine, StylesAPI):
    def __init__(self, text: str = ""):
        super().__init__("")
        self._palette          = Colors
        self.text              = text
        self._text_color       = ""
        self._background_color = ""
        self._text_style       = ""
        self._prefix           = ""

    """Dunder"""
    def __str__(self) -> str:
        return (
            f"{self._background_color}"
            f"{self._text_color}"
            f"{self._text_style}"
            f"{self._prefix}"
            f"{self.text}"
            f"\033[0m"
        )

    def __or__(self, other: str) -> "PrintLog":
        if other.startswith('#'):
            self._text_color = self.hex_to_rgb(other)
        else:
            self._text_color = self._set_text(other)
        return self

    def __add__(self, other) -> "PrintLog":
        self.text += other
        return self

    def __call__(self, text: str):
        self.text = text
        return self

    """API"""
    ## Foreground and Background colors
    def color(self, color: str) -> "PrintLog":
        if color.startswith("#"):
            self._text_color = self.hex_to_rgb(color)
        else:
            self._text_color = self._set_text(color)

        return self

    def background(self, color: str) -> "PrintLog":
        if color.startswith("#"):
            self._background_color = self.hex_to_rgb(color, background=True)
        else:
            self._background_color = self._set_back(color)
        return self

    def reset(self) -> "PrintLog":
        self._text_color = self._set_text(self._palette.RESET)
        self._background_color = self._set_back(self._palette.RESET)
        return self

    @property
    def plain(self) -> str:
        return self.text

    def copy(self) -> "PrintLog":
        return copy(self)

    def prefix(self, prefix: str) -> "PrintLog":
        self._prefix = prefix
        return self