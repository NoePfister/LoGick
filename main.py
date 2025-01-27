import curses

from LGUI import App, Color, Styles

def main(screen):
    app = App(screen)
    app.set_cursor(False)
    app.clear()
    app.refresh()

    color = Color((255,0,0),(255,255,255), 1)
    app.add_component((10,10),"LoGick", color, (Styles.BOLD, Styles.UNDERLINE))

    # repeat even if it is resized
    while app.wait_for_key() == '\\':
        pass



if __name__ == "__main__":
    curses.wrapper(main)



