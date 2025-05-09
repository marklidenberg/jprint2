from typing import Any, Callable
import jsons

from jprint2.defaults import USE_DEFAULT, defaults

try:
    import ujson as json
except ImportError:
    import json


def jformat(
    value: Any,
    keep_strings: bool = USE_DEFAULT,
    formatter: Callable = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
):
    # - Process arguments

    keep_strings = (
        defaults["keep_strings"] if keep_strings is USE_DEFAULT else keep_strings
    )
    indent = defaults["indent"] if indent is USE_DEFAULT else indent
    sort_keys = defaults["sort_keys"] if sort_keys is USE_DEFAULT else sort_keys
    ensure_ascii = (
        defaults["ensure_ascii"] if ensure_ascii is USE_DEFAULT else ensure_ascii
    )
    formatter = defaults["formatter"] if formatter is USE_DEFAULT else formatter

    # - Return if keep_strings is True and value is a string

    if keep_strings and isinstance(value, str):
        return value

    # - Format and return

    return formatter(
        value,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=ensure_ascii,
    )


def test():
    assert jformat(1) == "1"
    assert jformat("1") == "1"
    assert jformat({"a": 1}) == '{"a": 1}'
    assert jformat({"a": 1}, keep_strings=True) == '{"a": 1}'
    assert jformat({"a": 1}, keep_strings=False) == '{"a": 1}'


if __name__ == "__main__":
    test()
