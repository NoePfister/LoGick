from enum import Enum

print(f"Welcome to LGUI version {0.1}")
import curses

class Styles(Enum):
    BOLD = curses.A_BOLD
    STANDOUT = curses.A_STANDOUT
    UNDERLINE = curses.A_UNDERLINE

class Color:
    def __init__(self, fg_color: tuple[int,int,int], bg_color: tuple[int,int,int], uuid: int) -> None:
        self.id = 2*(uuid + 20)
        del uuid
        curses.init_color(self.id, fg_color[0], fg_color[1], fg_color[2])
        curses.init_color(self.id+1, bg_color[0], bg_color[1], bg_color[2])

        curses.init_pair(self.id, self.id, self.id+1)

class App:
    def __init__(self, enable_color: bool=True):
        self.screen = curses.initscr()
        if enable_color:
            curses.start_color()

        self.screen.clear()

        self.dimension = self.screen.getmaxyx()

    @staticmethod
    def set_cursor(visible: bool) -> None:
        curses.curs_set(visible)

    def refresh(self) -> None:
        self.screen.refresh()

    def add_component(self, pos: tuple[int,int], text: str, color: Color, styles: tuple[Styles, ...]) -> None:
        style_combination = 0
        for style in styles:
            style_combination |= style.value

        self.screen.addstr(pos[0], pos[1],text, curses.color_pair(color.id) | style_combination)
        self.refresh()
    @staticmethod
    def exit() -> None:
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()

    def clear(self) -> None:
        self.screen.clear()

    def wait_for_key(self) -> str:
        return chr(self.screen.getch())