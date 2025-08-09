import json
from typing import Any, Callable
import jsons


def default_formatter(
    value: Any,
    # - json.dumps arguments
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    cls: json.JSONEncoder,
    indent: int,
    separators: tuple,
    default: Callable,
    sort_keys: bool,
) -> str:
    # - Try to parse as JSON before formatting

    if isinstance(value, str):
        try:
            value = json.loads(value)
        except:
            # return string object as is
            return value

    # - Return formatted value

    return jsons.dumps(
        value,
        jdkwargs=dict(
            skipkeys=skipkeys,
            ensure_ascii=ensure_ascii,
            check_circular=check_circular,
            allow_nan=allow_nan,
            cls=cls,
            indent=indent,
            separators=separators,
            default=default,
            sort_keys=sort_keys,
        ),
    )
