import curses
from enum import Enum


class Styles(Enum):
    BOLD = curses.A_BOLD
    STANDOUT = curses.A_STANDOUT
    UNDERLINE = curses.A_UNDERLINE
