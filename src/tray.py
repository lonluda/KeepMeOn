import os
import sys
import pystray

from PIL import Image
from src.winlib import keep_awake, restore_normal_behavior


class TrayApp:

    def __init__(self):
        self.active = True

        self.icon = pystray.Icon(
            "KeepMeOn",
            self.create_icon(),
            "KeepMeOn",
            menu=self.create_menu()
        )

    def create_icon(self):
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        icon_path = os.path.join(base_path, "icon.png")

        return Image.open(icon_path)

    def about(self):
        pass

    def create_menu(self):
        return pystray.Menu(
            pystray.MenuItem(
                "Mantieni il PC attivo",
                self.toggle_awake,
                checked=lambda item: self.active
            ),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(
                "KeepMeOn v0.1 - LDL",
                self.about
            ),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(
                "Esci",
                self.exit_app
            )
        )

    def toggle_awake(self, icon, item):
        self.active = not self.active

        if self.active:
            keep_awake()
        else:
            restore_normal_behavior()

        icon.update_menu()

    def exit_app(self, icon, item):
        restore_normal_behavior()
        icon.stop()

    def run(self):
        keep_awake()
        self.icon.run()