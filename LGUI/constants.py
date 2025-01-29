import curses
from enum import Enum


class Styles(Enum):
    BOLD = curses.A_BOLD
    STANDOUT = curses.A_STANDOUT
    UNDERLINE = curses.A_UNDERLINE


class Alignments(Enum):
    UNSET = 0
    START = 1
    END = 2
    CENTRE = 3
    TOP = 4
    BOTTOM = 5
