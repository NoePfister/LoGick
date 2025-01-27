from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LGUI import ColorPair, Styles


class Component:
    def __init__(self, pos: tuple[int, int], text: str, color_pair: 'ColorPair', styles: tuple['Styles', ...] = ()):
        self.pos = pos
        self.text = text
        self.color_pair = color_pair
        self.styles = styles
