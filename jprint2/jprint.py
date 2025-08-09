import builtins
import json

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from typing import Union, Any, Callable
import sys

from jprint2.defaults.use_default import USE_DEFAULT
from jprint2.jformat import jformat


def jprint(
    # - Print options
    *objects,
    sep=" ",
    end="\n",
    file=sys.stdout,
    flush=False,
    # - Colorize options
    colorize: bool = True,
    # - Formatter
    formatter: Callable = USE_DEFAULT,
    # - Json.dumps arguments
    skipkeys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
    check_circular: bool = USE_DEFAULT,
    allow_nan: bool = USE_DEFAULT,
    cls: json.JSONEncoder = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    separators: tuple = USE_DEFAULT,
    default: Callable = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
):
    """Drop-in replacement for print with json formatting."""

    # - Get json string

    json_string = jformat(
        objects if len(objects) > 1 else objects[0],
        formatter=formatter,
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        cls=cls,
        indent=indent,
        separators=separators,
        default=default,
        sort_keys=sort_keys,
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

    builtin_print = (
        builtins.__builtin_print__ if hasattr(builtins, "__builtin_print__") else print
    )

    # -- Print

    builtin_print(
        json_string.strip(),
        sep=sep,
        end=end,
        file=file,
        flush=flush,
    )


def example():
    jprint({"name": "Mark", "age": 30})
    jprint("a", "b", "c")


if __name__ == "__main__":
    example()
