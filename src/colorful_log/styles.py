from typing_extensions import Self

class Styles:
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"

class StylesAPI:
    def __init__(self, text_style: str):
        self._text_style = text_style
        self._styles = Styles()

    def bold(self) -> Self:
        self._text_style += self._styles.BOLD
        return self

    def italic(self) -> Self:
        self._text_style += self._styles.ITALIC
        return self

    def underline(self) -> Self:
        self._text_style += self._styles.UNDERLINE
        return self

    def revert(self) -> Self:
        self._text_style += self._styles.REVERSE
        return self

    def dim(self) -> Self:
        self._text_style += self._styles.DIM
        return self

    def strikethrough(self) -> Self:
        self._text_style += self._styles.STRIKETHROUGH
        return self