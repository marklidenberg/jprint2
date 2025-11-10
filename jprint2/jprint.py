"""Simple JSON printer for Python."""

import json
from typing import Any

try:
    import jsons
except ImportError:
    jsons = None  # type: ignore

from pygments import highlight
from pygments.lexers import JsonLexer  # type: ignore
from pygments.formatters import TerminalFormatter  # type: ignore


def jprint(*objects: Any, indent: bool = True) -> None:
    """Print objects as formatted, colorized JSON.

    Args:
        *objects: Objects to print. If multiple objects are provided, they are printed as a list.
        indent: Whether to indent the JSON output. Default is True (indent with 2 spaces).
    """

    # - Handle single vs multiple objects

    value = objects[0] if len(objects) == 1 else list(objects)

    # - Convert to JSON-serializable format using jsons if available

    if jsons is not None:
        try:
            value = jsons.dump(value)
        except Exception:
            pass  # Fall back to standard json serialization

    # - Convert to JSON string

    json_string = json.dumps(
        value,
        indent=2 if indent else None,
        default=str,  # Fallback for non-serializable objects
        ensure_ascii=False,
    )

    # - Colorize the output

    colored_output = highlight(
        code=json_string,
        lexer=JsonLexer(),
        formatter=TerminalFormatter(),
    )

    # - Print the result

    print(colored_output.strip())


def example():
    """Example usage of jprint."""
    jprint({"name": "Mark", "age": 30})
    jprint("a", "b", "c")
    jprint({"name": "Mark", "age": 30}, indent=False)


if __name__ == "__main__":
    example()
