import curses

from LGUI import App, Component, Color, ColorPair, Styles
from LGUI.components.label import Label
from LGUI.constants import Alignments


def main(screen):
    app = App(screen)
    app.set_cursor(False)
    app.clear()
    app.refresh()

    black = Color((0, 0, 0), 2)
    white = Color((1000, 1000, 1000), 3)

    green_gray = ColorPair(black, white, 2)

    label_end = Label("Ende", 8, Alignments.END, green_gray, (Styles.UNDERLINE, Styles.BOLD))
    label_start = Label("start", 9, Alignments.START, green_gray, (Styles.UNDERLINE, Styles.BOLD))
    label_centre = Label("centre", 10, Alignments.CENTRE, green_gray, (Styles.UNDERLINE, Styles.BOLD))

    app.add_component(label_end)
    app.add_component(label_start)
    app.add_component(label_centre)

    while True:
        key = app.wait_for_key()
        print(key)
        if key == 'q':
            app.exit()
            return


if __name__ == "__main__":
    curses.wrapper(main)
