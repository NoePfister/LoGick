import curses


class Color:
    def __init__(self, color: tuple[int, int, int], index: int) -> None:
        self.index = index + 15
        self.color = color

        curses.init_color(self.index, color[0], color[1], color[2])


class ColorPair:
    def __init__(self, fg: Color, bg: Color, index: int):
        self.index = index + 15
        self.fg = fg
        self.bg = bg

        curses.init_pair(self.index, fg.index, bg.index)
