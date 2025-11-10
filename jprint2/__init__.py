"""Simple JSON printer for Python."""

from importlib.metadata import version

try:
    __version__ = version("jprint2")
except Exception:
    __version__ = "unknown"

from .jprint import jprint

__all__ = [
    "__version__",
    "jprint",
]
