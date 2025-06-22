from typing import Any, Callable
import jsons

from jprint2.defaults import USE_DEFAULT, defaults, get_default, set_defaults

try:
    import ujson as json  # type: ignore
except ImportError:
    import json


def jformat(
    value: Any,
    formatter: Callable = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
):
    # - Process arguments

    indent = get_default(
        "indent",
        provided=indent,
    )
    sort_keys = get_default(
        "sort_keys",
        provided=sort_keys,
    )
    ensure_ascii = get_default(
        "ensure_ascii",
        provided=ensure_ascii,
    )
    formatter = get_default(
        "formatter",
        provided=formatter,
    )

    # - Format and return

    return formatter(
        value,
        indent=indent,
        sort_keys=sort_keys,
        ensure_ascii=ensure_ascii,
    )


def test():
    set_defaults(indent=None)
    assert jformat(1) == "1"
    assert jformat("1") == "1"
    assert jformat({"a": 1}) == '{"a": 1}'


if __name__ == "__main__":
    test()
