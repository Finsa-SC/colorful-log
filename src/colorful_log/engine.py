class PrintLogEngine:
    @staticmethod
    def _set_text(num: str) -> str:
        return f"\033[3{num}m"

    @staticmethod
    def _set_back(num: str) -> str:
        return f"\033[4{num}m"

    @staticmethod
    def hex_to_rgb(hex_color: str, background: bool = False) -> str:
        hex_color = hex_color.lstrip('#')

        if len(hex_color) < 6:
            raise ValueError("HEX color must contain 6 digits.")

        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        code = "4" if background else "3"

        return f"\033[{code}8;2;{r};{g};{b}m"