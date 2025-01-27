import curses

from LGUI.color import Color, ColorPair
from LGUI.constants import Styles
from LGUI.component import Component

print(f"Welcome to LGUI version {0.1}")


class App:
    def __init__(self, screen, enable_color: bool = True):
        self.screen = screen
        if enable_color:
            curses.start_color()

        self.screen.clear()

        self.dimension = self.screen.getmaxyx()
        self.components: list[Component] = []

    @staticmethod
    def set_cursor(visible: bool) -> None:
        curses.curs_set(visible)

    def refresh(self) -> None:
        self.clear()
        for comp in self.components:
            style_combination = 0
            for style in comp.styles:
                style_combination |= style.value

            self.screen.addstr(comp.pos[0], comp.pos[1], comp.text,
                               curses.color_pair(comp.color_pair.index) | style_combination)
        self.screen.refresh()

    def add_component(self, comp: Component) -> None:
        self.components.append(comp)
        self.refresh()

    def exit(self) -> None:
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        self.screen.clear()
        self.screen.refresh()
        curses.endwin()

    def clear(self) -> None:
        self.screen.clear()

    def wait_for_key(self) -> str:
        """

        :return: The key pressed as a char.

        - **KeyboardInterrupt**: '?'
        - **Resize**: '!'
        """
        try:
            key = self.screen.getch()
            if key == curses.KEY_RESIZE:
                self.resize()
                key = ord('!')
            self.refresh()

        except KeyboardInterrupt:
            key = ord('?')

        return chr(key)

    def resize(self):
        self.dimension = self.screen.getmaxyx()
        self.screen.clear()
        curses.resize_term(self.dimension[0], self.dimension[1])
        self.screen.refresh()
