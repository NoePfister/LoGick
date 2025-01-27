from enum import Enum

print(f"Welcome to LGUI version {0.1}")
import curses


class Styles(Enum):
    BOLD = curses.A_BOLD
    STANDOUT = curses.A_STANDOUT
    UNDERLINE = curses.A_UNDERLINE


class Color:
    def __init__(self, fg_color: tuple[int, int, int], bg_color: tuple[int, int, int], uuid: int) -> None:
        self.id = 2 * (uuid + 20)
        del uuid
        curses.init_color(self.id, fg_color[0], fg_color[1], fg_color[2])
        curses.init_color(self.id + 1, bg_color[0], bg_color[1], bg_color[2])

        curses.init_pair(self.id, self.id, self.id + 1)


class App:
    def __init__(self, screen, enable_color: bool = True):
        self.screen = screen
        if enable_color:
            curses.start_color()

        self.screen.clear()

        self.dimension = self.screen.getmaxyx()
        self.components: list[tuple[
            tuple[int, int],
            str,
            Color,
            tuple[Styles, ...]]] = []

    @staticmethod
    def set_cursor(visible: bool) -> None:
        curses.curs_set(visible)

    def refresh(self) -> None:
        self.clear()
        for component in self.components:
            style_combination = 0
            for style in component[3]:
                style_combination |= style.value

            self.screen.addstr(component[0][0], component[0][1], component[1],
                               curses.color_pair(component[2].id) | style_combination)
        self.screen.refresh()

    def add_component(self, pos: tuple[int, int], text: str, color: Color, styles: tuple[Styles, ...]) -> None:
        self.components.append((pos, text, color, styles))
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

        try:
            key = self.screen.getch()
            if key == curses.KEY_RESIZE:
                color = Color((255, 0, 0), (255, 255, 255), 2)
                self.add_component((5, 10), "Resize", color, (Styles.BOLD, Styles.UNDERLINE))
                self.resize()
                key = ord('\\')
            self.refresh()
            return chr(key)
        except KeyboardInterrupt:
            self.exit()
            return '\\'

    def resize(self):
        self.dimension = self.screen.getmaxyx()
        self.screen.clear()
        curses.resize_term(self.dimension[0], self.dimension[1])
        self.screen.refresh()
