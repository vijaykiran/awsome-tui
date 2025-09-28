from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from awsome.cli import cli


class TestCLI:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_cli_help(self) -> None:
        result = self.runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "AWSome - Terminal User Interface for AWS" in result.output
        assert "--config" in result.output
        assert "--profile" in result.output
        assert "--region" in result.output
        assert "--debug" in result.output

    @patch("awsome.cli.AWSomeApp")
    def test_cli_with_no_options(self, mock_app_class: MagicMock) -> None:
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app

        result = self.runner.invoke(cli, [])

        assert result.exit_code == 0
        mock_app_class.assert_called_once_with(
            config={
                "config_file": None,
                "profile": None,
                "region": None,
                "debug": False,
            }
        )
        mock_app.run.assert_called_once()

    @patch("awsome.cli.AWSomeApp")
    def test_cli_with_profile(self, mock_app_class: MagicMock) -> None:
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app

        result = self.runner.invoke(cli, ["--profile", "production"])

        assert result.exit_code == 0
        mock_app_class.assert_called_once_with(
            config={
                "config_file": None,
                "profile": "production",
                "region": None,
                "debug": False,
            }
        )
        mock_app.run.assert_called_once()

    @patch("awsome.cli.AWSomeApp")
    def test_cli_with_region(self, mock_app_class: MagicMock) -> None:
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app

        result = self.runner.invoke(cli, ["--region", "us-west-2"])

        assert result.exit_code == 0
        mock_app_class.assert_called_once_with(
            config={
                "config_file": None,
                "profile": None,
                "region": "us-west-2",
                "debug": False,
            }
        )
        mock_app.run.assert_called_once()

    @patch("awsome.cli.AWSomeApp")
    def test_cli_with_debug(self, mock_app_class: MagicMock) -> None:
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app

        result = self.runner.invoke(cli, ["--debug"])

        assert result.exit_code == 0
        mock_app_class.assert_called_once_with(
            config={
                "config_file": None,
                "profile": None,
                "region": None,
                "debug": True,
            }
        )
        mock_app.run.assert_called_once()

    @patch("awsome.cli.AWSomeApp")
    def test_cli_with_all_options(self, mock_app_class: MagicMock) -> None:
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app

        with self.runner.isolated_filesystem():
            with open("config.yaml", "w") as f:
                f.write("test: config")

            result = self.runner.invoke(
                cli,
                [
                    "--config",
                    "config.yaml",
                    "--profile",
                    "dev",
                    "--region",
                    "eu-west-1",
                    "--debug",
                ],
            )

            assert result.exit_code == 0
            mock_app_class.assert_called_once_with(
                config={
                    "config_file": "config.yaml",
                    "profile": "dev",
                    "region": "eu-west-1",
                    "debug": True,
                }
            )
            mock_app.run.assert_called_once()

    def test_cli_with_nonexistent_config(self) -> None:
        result = self.runner.invoke(cli, ["--config", "nonexistent.yaml"])
        assert result.exit_code != 0
        assert "does not exist" in result.output.lower()

    @patch("awsome.cli.AWSomeApp")
    def test_cli_short_options(self, mock_app_class: MagicMock) -> None:
        mock_app = MagicMock()
        mock_app_class.return_value = mock_app

        result = self.runner.invoke(cli, ["-p", "prod", "-r", "us-east-1"])

        assert result.exit_code == 0
        mock_app_class.assert_called_once_with(
            config={
                "config_file": None,
                "profile": "prod",
                "region": "us-east-1",
                "debug": False,
            }
        )
        mock_app.run.assert_called_once()
