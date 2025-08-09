from typing import Any
from jprint2.defaults.defaults import defaults
from jprint2.defaults.use_default import USE_DEFAULT


def get_default(
    key: str,
    provided: Any = USE_DEFAULT,
):
    return defaults[key] if provided is USE_DEFAULT else provided
