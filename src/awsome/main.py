from typing import Any, override

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class AWSomeApp(App):
    TITLE = "AWSome"

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        super().__init__()
        self.config = config or {}
        self.aws_profile = self.config.get("profile")
        self.aws_region = self.config.get("region")
        self.debug_mode = self.config.get("debug", False)
        self.config_file = self.config.get("config_file")

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
