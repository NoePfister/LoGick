from LGUI import App, Color, Styles

def main():
    app = App()
    app.set_cursor(False)
    app.clear()
    app.refresh()

    color = Color((255,0,0),(255,255,255), 1)
    app.add_component((10,10),"LoGick", color, (Styles.BOLD, Styles.UNDERLINE))

    print(app.wait_for_key())


if __name__ == "__main__":
    main()



