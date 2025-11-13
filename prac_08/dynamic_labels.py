"""
CP1404
Dynamic Labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Simple app that dynamically creates labels from a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Model: list of names (strings)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Evan"]

    def build(self):
        """Build the GUI and add labels dynamically."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add it to the layout."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
