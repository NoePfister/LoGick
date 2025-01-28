import curses

from LGUI import Component
from LGUI.constants import Alignments

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LGUI import ColorPair, Styles


class Label(Component):
    def __init__(self, text: str, pos_y: int, align: Alignments, color_pair: 'ColorPair',
                 styles: tuple['Styles', ...] = ()):
        self.alignment = align
        self.pos_y = pos_y
        self.text = text

        self.compute_pos()

        super().__init__(self.pos, text, color_pair, styles)

    def compute_pos(self) -> None:
        match self.alignment:
            case Alignments.START:
                self.pos = (0, self.pos_y)
            case Alignments.END:
                self.pos = (curses.COLS - len(self.text), self.pos_y)
                print(curses.COLS, self.pos)
            case Alignments.CENTRE:
                self.pos = (curses.COLS // 2 - len(self.text) // 2, self.pos_y)
