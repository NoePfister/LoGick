import curses

from LGUI.color import Color, ColorPair
from LGUI.constants import Styles
from LGUI.component import Component
from LGUI.components.label import Label

print(f"Welcome to LGUI version {0.1}")


class TUI:
    def __init__(self, screen, enable_color: bool = True):
        self.screen = screen
        curses.raw()
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

            # check if the component can recompute the position
            compute_pos = getattr(comp, "compute_pos", None)
            if callable(compute_pos):
                comp.compute_pos()  # type: ignore

            style_combination = 0
            for style in comp.styles:
                style_combination |= style.value

            max_y, max_x = self.screen.getmaxyx()
            if comp.pos[1] >= max_y or comp.pos[0] + len(comp.text) >= max_x:
                raise Exception(f"Text to big: {comp.pos} max: {max_x, max_y}")

            # X and Y are in wrong order for dome reason. It is being corrected here
            self.screen.addstr(comp.pos[1], comp.pos[0], comp.text,
                               (curses.color_pair(comp.color_pair.index) | style_combination))
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
        exit(0)

    def clear(self) -> None:
        self.screen.clear()

    def clean_screen(self):
        self.components.clear()
        self.clear()

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

        return key

    def resize(self):
        self.dimension = self.screen.getmaxyx()
        self.screen.clear()
        curses.resize_term(self.dimension[0], self.dimension[1])
        self.screen.refresh()
