from typing import override

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class AWSomeApp(App):
    TITLE = "AWSome"

    @override
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()


def start() -> None:
    # Create and run the application
    app = AWSomeApp()
    # Run the application
    app.run()


if __name__ == "__main__":
    start()
