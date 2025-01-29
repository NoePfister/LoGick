import curses

from LGUI import Component
from LGUI.constants import Alignments

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from LGUI import ColorPair, Styles


class Label(Component):
    def __init__(self,
                 text: str,
                 color_pair: 'ColorPair',
                 pos_offset: tuple[int, int] = (0, 0),
                 alignment: tuple[Alignments, Alignments] = (Alignments.UNSET, Alignments.UNSET),
                 styles: tuple['Styles', ...] = ()):

        self.alignment = alignment
        self.pos_offset = pos_offset
        self.pos = [0, 0]
        self.text = text

        self.compute_pos()

        super().__init__(self.pos, text, color_pair, styles)

    def compute_pos(self) -> None:
        self.pos = [0, 0]

        # X coordinate
        match self.alignment[0]:
            case Alignments.START:
                self.pos[0] = 0 + self.pos_offset[0]
            case Alignments.END:
                self.pos[0] = curses.COLS - len(self.text) + self.pos_offset[0]
            case Alignments.CENTRE:
                self.pos[0] = (curses.COLS // 2) - (len(self.text) // 2) + self.pos_offset[0]
            case Alignments.UNSET:
                self.pos[0] = self.pos_offset[0]
            case _:
                raise Exception(f'Alignment option {self.alignment[0]} is not available for horizontal Alignment')

        # Y coordinate
        match self.alignment[1]:
            case Alignments.TOP:
                self.pos[1] = 0 + self.pos_offset[1]
            case Alignments.BOTTOM:
                self.pos[1] = curses.LINES + self.pos_offset[1] - 1
            case Alignments.CENTRE:
                self.pos[1] = (curses.LINES // 2) + self.pos_offset[1]
            case Alignments.UNSET:
                self.pos[1] = self.pos_offset[1]
            case _:
                raise Exception(f'Alignment option {self.alignment[1]} is not available for vertical Alignment')
