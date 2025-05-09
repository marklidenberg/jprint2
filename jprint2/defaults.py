from typing import Callable, Any

import jsons


def default_formatter(
    value: Any,
    indent: int = None,
    sort_keys: bool = False,
    ensure_ascii: bool = False,
):
    return jsons.dumps(
        value,
        jdkwargs=dict(
            indent=indent,
            sort_keys=sort_keys,
            ensure_ascii=ensure_ascii,
        ),
    )


defaults = {
    "keep_strings": True,
    "indent": None,
    "sort_keys": False,
    "ensure_ascii": False,
    "formatter": default_formatter,
}

USE_DEFAULT = object()


def set_defaults(
    keep_strings: bool = False,
    indent: int = 4,
    sort_keys: bool = False,
    ensure_ascii: bool = False,
    formatter: Callable = jsons.dumps,
):
    defaults["keep_strings"] = keep_strings
    defaults["indent"] = indent
    defaults["sort_keys"] = sort_keys
    defaults["ensure_ascii"] = ensure_ascii
    defaults["formatter"] = formatter
    return defaults
