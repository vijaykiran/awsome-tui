
import click

from awsome.main import AWSomeApp


@click.command()
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True),
    help="Path to configuration file",
)
@click.option("--profile", "-p", help="AWS profile to use")
@click.option("--region", "-r", help="AWS region")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def cli(
    config: str | None,
    profile: str | None,
    region: str | None,
    debug: bool,
) -> None:
    """AWSome - Terminal User Interface for AWS."""
    app_config = {
        "config_file": config,
        "profile": profile,
        "region": region,
        "debug": debug,
    }

    app = AWSomeApp(config=app_config)
    app.run()


if __name__ == "__main__":
    cli()
