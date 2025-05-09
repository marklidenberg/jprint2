from importlib.metadata import version

try:
    __version__ = version("dony")
except Exception:
    __version__ = "unknown"

from .defaults import set_defaults, defaults
from .jformat import jformat
from .jprint import jprint
