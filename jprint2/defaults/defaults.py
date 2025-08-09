import json
from typing import Any, Callable, Optional

from jprint2.defaults.default_formatter import default_formatter


# - Define defaults

defaults = {}

# - Set defaults


def set_defaults(
    formatter: Callable = default_formatter,
    # - json.dumps arguments
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: json.JSONEncoder = None,
    indent: Optional[int] = 2,
    separators: tuple = None,
    default: Callable = str,
    sort_keys: bool = False,
):
    defaults["formatter"] = formatter
    defaults["skipkeys"] = skipkeys
    defaults["ensure_ascii"] = ensure_ascii
    defaults["check_circular"] = check_circular
    defaults["allow_nan"] = allow_nan
    defaults["cls"] = cls
    defaults["indent"] = indent
    defaults["separators"] = separators
    defaults["default"] = default
    defaults["sort_keys"] = sort_keys


set_defaults()
