from json import JSONEncoder
from typing import Any, Callable
import jsons

from jprint2.defaults.get_default import get_default
from jprint2.defaults.use_default import USE_DEFAULT


try:
    import ujson as json  # type: ignore
except ImportError:
    import json


def jformat(
    value: Any,
    formatter: Callable = USE_DEFAULT,
    # - Json.dumps arguments
    skipkeys: bool = USE_DEFAULT,
    ensure_ascii: bool = USE_DEFAULT,
    check_circular: bool = USE_DEFAULT,
    allow_nan: bool = USE_DEFAULT,
    cls: JSONEncoder = USE_DEFAULT,
    indent: int = USE_DEFAULT,
    separators: tuple = USE_DEFAULT,
    default: Callable = USE_DEFAULT,
    sort_keys: bool = USE_DEFAULT,
):
    return get_default(
        "formatter",
        provided=formatter,
    )(
        value,
        skipkeys=get_default("skipkeys", provided=skipkeys),
        ensure_ascii=get_default("ensure_ascii", provided=ensure_ascii),
        check_circular=get_default("check_circular", provided=check_circular),
        allow_nan=get_default("allow_nan", provided=allow_nan),
        cls=get_default("cls", provided=cls),
        indent=get_default("indent", provided=indent),
        separators=get_default("separators", provided=separators),
        default=get_default("default", provided=default),
        sort_keys=get_default("sort_keys", provided=sort_keys),
    )


def test():
    from jprint2.defaults.defaults import set_defaults

    set_defaults(indent=None)
    assert jformat(1) == "1"
    assert jformat("1") == "1"
    assert jformat({"a": 1}) == '{"a": 1}'


if __name__ == "__main__":
    test()
