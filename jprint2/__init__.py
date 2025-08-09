from importlib.metadata import version

try:
    __version__ = version("jprint2")
except Exception:
    __version__ = "unknown"

from .jformat import jformat
from .jprint import jprint
from .defaults.defaults import set_defaults
from .defaults.default_formatter import default_formatter
from .defaults.get_default import get_default
from .defaults.use_default import USE_DEFAULT
