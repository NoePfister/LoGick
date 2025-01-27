import curses

from LGUI import App, Component, Color, ColorPair


def main(screen):
    app = App(screen)
    app.set_cursor(False)
    app.clear()
    app.refresh()

    red = Color((255, 0, 0), 1)
    green = Color((0, 255, 0), 2)
    gray = Color((105, 105, 105), 3)

    red_gray = ColorPair(red, gray, 1)
    green_gray = ColorPair(green, gray, 2)

    app.add_component(Component((5, 5), 'Hello World', red_gray))
    app.add_component(Component((6, 5), 'Hello Green', green_gray))

    while True:
        key = app.wait_for_key()
        print(key)
        if key == 'q':
            app.exit()
            return


if __name__ == "__main__":
    curses.wrapper(main)
