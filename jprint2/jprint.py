import builtins

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from typing import Union, Any, Callable
from jprint2.defaults import defaults, USE_DEFAULT
import sys

from jprint2.jformat import jformat


def jprint(
    # - Print options
    *objects,
    sep=" ",
    end="\n",
    file=sys.stdout,
    flush=False,
    # - Json options
    formatter: Callable = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
    # - Colorize options
    colorize: bool = True,
):
    """Drop-in replacement for print with json formatting."""

    # - Get json string

    json_string = jformat(
        objects if len(objects) > 1 else objects[0],
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

    # -- Get original print (in case it was replaced with `replace_print_with_jprint`)

    orig_print = (
        builtins.__orig_print__ if hasattr(builtins, "__orig_print__") else print
    )

    # -- Print

    orig_print(
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
    jprint("a", "b", "c")
    print()


if __name__ == "__main__":
    example()
