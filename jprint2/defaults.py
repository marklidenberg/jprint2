from typing import Callable, Any

import jsons

try:
    import ujson as json
except ImportError:
    import json

# - USE_DEFAULT placeholder

USE_DEFAULT = object()

# - Set defaults


def default_formatter(
    value: Any,
    indent: int = None,
    sort_keys: bool = False,
    ensure_ascii: bool = False,
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
            indent=indent,
            sort_keys=sort_keys,
            ensure_ascii=ensure_ascii,
        ),
    )


defaults = {}


def set_defaults(
    indent: int = 2,
    sort_keys: bool = False,
    ensure_ascii: bool = False,
    formatter: Callable = default_formatter,
):
    defaults["indent"] = indent
    defaults["sort_keys"] = sort_keys
    defaults["ensure_ascii"] = ensure_ascii
    defaults["formatter"] = formatter
    return defaults


set_defaults()

# - Get defaults


def get_default(key: str, provided: Any = USE_DEFAULT):
    return defaults[key] if provided is USE_DEFAULT else provided
