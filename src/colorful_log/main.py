from colorful_log.engine import PrintLogEngine
from colorful_log.colors import Colors

class PrintLog(PrintLogEngine):
    def __init__(self, text: str):
        super().__init__()
        self.__palette          = Colors
        self.text               = text
        self.__text_color       = self.__palette.RESET
        self.__background_color = self.__palette.RESET


    """Dunder"""
    def __str__(self) -> str:
        return (
            f"{self.__background_color}"
            f"{self.__text_color}"
            f"{self.text}"
            f"{self.__palette.RESET}"
        )

    def __or__(self, other: str) -> "PrintLog":
        if other.startswith('#'):
            self.__text_color = self.hex_to_rgb(other)
        else:
            self.__text_color = self.__set_text(other)
        return self

    def __add__(self, other) -> "PrintLog":
        self.text += other
        return self

    """API"""
    def color(self, color: str) -> "PrintLog":
        if color.startswith("#"):
            self.__text_color = self.hex_to_rgb(color)
        else:
            self.__text_color = self.__set_text(color)

        return self

    def background(self, color: str) -> "PrintLog":
        if color.startswith("#"):
            self.__background_color = self.hex_to_rgb(color, background=True)
        else:
            self.__background_color = self.__set_back(color)
        return self

    def reset(self) -> "PrintLog":
        self.__text_color = self.__palette.RESET
        self.__background_color = self.__palette.RESET
        return self

if __name__ == "__main__":
    agus = PrintLog("Hello Agus!")
    print(agus | "#fff11f")
    print(agus.background("#1ff11f"))
    print(agus + " Apa kabar?")