from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from typing import Union, Any, Callable
from jprint2.defaults import defaults, USE_DEFAULT
from jprint2.jformat import jformat
import sys


def jprint(
    # - Print options
    *objects,
    sep=" ",
    end="\n",
    file=sys.stdout,
    flush=False,
    # - Json options
    keep_strings: bool = USE_DEFAULT,
    formatter: Callable = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
    colorize: bool = True,
):
    """Pretty"""

    # - Get json string

    json_string = jformat(
        objects if len(objects) > 1 else objects[0],
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

    print(
        json_string.strip(),
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )


def example():
    print()
    import json

    jprint({"name": "Mark", "age": 30}, formatter=json.dumps)
    jprint('{"name": "Mark"}', keep_strings=False)


if __name__ == "__main__":
    example()
