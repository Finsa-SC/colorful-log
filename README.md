# colorful-log

[![PyPI version](https://img.shields.io/pypi/v/colorful-log)](https://pypi.org/project/colorful-log/)
[![Python versions](https://img.shields.io/pypi/pyversions/colorful-log)](https://pypi.org/project/colorful-log/)
[![License](https://img.shields.io/github/license/Finsa-SC/colorfull-log)](LICENSE)

A small Python library for coloring and styling terminal text, without writing raw ANSI escape codes by hand.

```python
from colorful_log import PrintLog, Colors

print(PrintLog("Build succeeded").color(Colors.GREEN).bold())
```

## Why colorful-log?

Terminal colors are done with escape sequences like `\033[1;32m`, which are hard to read, easy to get wrong, and easy to forget to reset. colorful-log wraps them in a small, readable API:

- **Readable code.** `PrintLog("Done").color(Colors.GREEN).bold()` says what it does. No escape codes to memorize.
- **Hex colors out of the box.** Use `"#6381f6"` directly, for both text and background.
- **Reusable styles.** Build a template once (for example an "error" style) and reuse it for any text.
- **Lightweight.** One small dependency (`typing-extensions`), fully typed, and works on Python 3.10+.

## Installation

```bash
pip install colorful-log
```

Requires Python 3.10 or newer.

## Features

- Foreground and background colors from built-in colors, hex codes, or your own registered colors
- Text styles: bold, dim, italic, underline, reverse, and strikethrough
- Method chaining and a short `|` operator for setting the text color
- Reusable templates with `copy()`, and an easy way to swap the text with a call
- Custom color registry, which can also override built-in colors
- `plain` property to get the text without any formatting
- Separate resets for colors (`reset()`) and styles (`reset_style()`)
- Clear `ValueError` for invalid hex colors

## Usage

### Basic

```python
from colorful_log import PrintLog, Colors

print(PrintLog("Hello, World!").color(Colors.CYAN))
print(PrintLog("Hello, World!").color("#6381f6").background("#1e1e2e"))
```

Built-in colors: `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`.

### Text styles

Styles can be chained in any order.

```python
PrintLog("Important").bold().underline()
PrintLog("Deprecated").dim().strikethrough()
```

Available styles: `bold()`, `dim()`, `italic()`, `underline()`, `revert()` (reverse video), `strikethrough()`.

### Setting the color with `|`

The `|` operator is a shortcut for setting the text color.

```python
print(PrintLog("Warning: disk almost full") | Colors.YELLOW)
print(PrintLog("Custom") | "#ff8800")
```

### Custom colors

Register a color once and use it anywhere.

```python
Colors.register("brand", "#6381f6")

print(PrintLog("Brand color") | Colors.brand)
```

Registering a name that already exists replaces it, including the built-in colors:

```python
Colors.register("RED", "#ff5555")   # Colors.RED is now #ff5555
```

This is global, so it affects every use of `Colors.RED` in your program.
`RESET`, `register`, and names starting with `_` are reserved and raise a `ValueError`.

### Templates

Calling a `PrintLog` instance replaces its text and keeps its formatting, so you can define a style once and reuse it.

```python
error = PrintLog().color(Colors.WHITE).background(Colors.RED).bold()

print(error("Something went wrong"))
print(error("Another error"))
```

> Calling an instance (and using `+`) modifies that same object and returns it.
> If you need independent results, use `copy()`:
>
> ```python
> a = error.copy()("First")
> b = error.copy()("Second")
> ```

### Appending text

```python
msg = PrintLog("Hello")
print(msg + ", World!")      # appends to the existing text
```

### Plain text

`plain` returns the text without any color or style codes, which is useful for logs or files.

```python
error("Disk full").plain     # "Disk full"
```

### Resetting

```python
style = PrintLog("text").bold().color(Colors.RED)

style.reset()          # clears foreground and background colors, keeps styles
style.reset_style()    # clears text styles, keeps colors
```

### Invalid colors

Invalid hex values raise a `ValueError` with a clear message.

```python
PrintLog("x") | "#GGGGGG"
# ValueError: Invalid HEX color: '#GGGGGG'. Expected format: '#RRGGBB'.
```

Only the `#RRGGBB` format is supported.

## Notes

- Hex colors use 24-bit ("truecolor") ANSI codes. Most modern terminals support them, but some older ones do not.
- Output contains ANSI escape codes. Use `.plain` if you need clean text, for example when writing to a file.

## License

Released under the [MIT License](LICENSE).

## Author

Finsa Kusuma Putra ([@Finsa-SC](https://github.com/Finsa-SC))