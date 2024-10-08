import click

from cycloplanning import create_ics, get_html, parse_events, parse_html, write_ics

CYCLOPLANNING_URL = "https://lite.framacalc.org/cycloplanning.html"


@click.command()
@click.option(
    "-o",
    "--output",
    help="file to write ICS to",
    type=click.STRING,
    default="/dev/stdout",
)
@click.option(
    "--url",
    help="URL to parse cycloplanning from",
    type=click.STRING,
    default=CYCLOPLANNING_URL,
)
@click.version_option(package_name="cycloplanning")
def main(output: str, url: str):
    write_ics(create_ics(parse_events(parse_html(get_html(url)))), output)


if __name__ == "__main__":
    main()
