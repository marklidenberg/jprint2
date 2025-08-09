import builtins

from jprint2 import jprint

"""
Import this file to replace print with jprint.
"""

builtins.__builtin_print__ = builtins.print
builtins.print = jprint

if __name__ == "__main__":
    print("Hello", "World")
