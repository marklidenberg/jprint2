import builtins

from jprint2 import jprint

"""
Import this file to replace print with jprint.
"""

builtins.__orig_print__ = builtins.print
builtins.print = jprint
