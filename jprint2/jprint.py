from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from typing import Union, Any, Callable
from jprint2.defaults import defaults, USE_DEFAULT
from jprint2.jformat import jformat


def jprint(
    value: Any,
    keep_strings: bool = USE_DEFAULT,
    formatter: Callable = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
    colorize: bool = True,
):
    # - Get json string

    json_string = jformat(
        value,
        keep_strings=keep_strings,
        formatter=formatter,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=ensure_ascii,
    )

    # - Colorize if needed

    if colorize:
        json_string = highlight(
            code=json_string,
            lexer=JsonLexer(),
            formatter=TerminalFormatter(),
        )

    # - Print

    print(json_string.strip())


def example():
    print()
    import json

    jprint({"name": "Mark", "age": 30}, formatter=json.dumps)
    jprint('{"name": "Mark"}', keep_strings=False)


if __name__ == "__main__":
    example()
