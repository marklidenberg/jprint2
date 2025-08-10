import builtins

from jprint2 import jprint

"""
Import this file to replace print with jprint.
"""


def override_print():
    builtins.__builtin_print__ = builtins.print
    builtins.print = jprint


def restore_print():
    builtins.print = getattr(builtins, "__builtin_print__", print)


if __name__ == "__main__":
    override_print()
    print("Hello", "World")
