import curses

from LGUI import TUI, Color, ColorPair, Styles, Component
from LGUI.components.label import Label
from LGUI.constants import Alignments

DATA = {
    "Helix": {"PC": "D://", "NATEl": "/mnt"},
    "Nvim": {"PC": "C://", "LAPtop": "/tmp"},
}


def clamp(val: int, min: int, max: int) -> int:
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val


class Application:
    def __init__(self, screen):
        self.tui = TUI(screen)
        self.tui.set_cursor(False)
        self.tui.refresh()

        self.devices: list[str] = []
        self.device_comps: list[Component] = []

        self.selected = 0

        # Init Colors
        black = Color((0, 0, 0), 1)
        white = Color((1000, 1000, 1000), 2)
        gray = Color((200, 200, 200), 3)

        self.normal_color = ColorPair(black, gray, 2)
        self.highlight_color = ColorPair(black, white, 3)

        self.device_select_screen()

    def device_select_screen(self) -> None:
        self.tui.clean_screen()
        title = Label("LoGick - Select your current device", 1, Alignments.CENTRE, self.normal_color)
        self.tui.add_component(title)

        self.devices = self.get_devices()

        for device in self.devices:
            self.device_comps.append(
                Label(f'    - {device}', self.devices.index(device) + 5, Alignments.START, self.normal_color))

        for comp in self.device_comps:
            self.tui.add_component(comp)

        self.update_highlighted_device()

        while True:
            key = self.tui.wait_for_key()
            if key == ord('q'):
                self.tui.exit()
            if key == curses.KEY_UP:  # Arrow Up
                self.selected = clamp(self.selected - 1, 0, 2)
                self.update_highlighted_device()
            if key == curses.KEY_DOWN:  # Arrow Down

                self.selected = clamp(self.selected + 1, 0, 2)
                self.update_highlighted_device()
            if key == 13:  # Enter key
                self.config_selection_screen()

    def config_selection_screen(self) -> None:
        self.tui.clean_screen()

        selected_device = self.devices[self.selected]

        title = Label("LoGick - Select the Config you want to sync", 1, Alignments.CENTRE, self.normal_color)
        self.tui.add_component(title)

        selected_device_label = Label(f"Device Selected: {selected_device}", 3, Alignments.START, self.normal_color)
        self.tui.add_component(selected_device_label)

        while True:
            key = self.tui.wait_for_key()
            if key == ord('q'):
                self.tui.exit()

    def update_highlighted_device(self) -> None:
        for comp in self.device_comps:
            if self.device_comps[self.selected] == comp:  # If comp is the selected one
                comp.color_pair = self.highlight_color
            else:
                comp.color_pair = self.normal_color

        self.tui.refresh()

    @staticmethod
    def get_devices() -> list[str]:
        devices = []
        for config_name in DATA:
            for device_name in DATA[config_name]:
                if not device_name in devices:
                    devices.append(device_name)

        return devices


def main(screen):
    app = Application(screen)


if __name__ == "__main__":
    curses.wrapper(main)
