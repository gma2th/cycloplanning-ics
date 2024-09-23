# Cycloplanning

Parse cycloplanning framacalc as ICS

## Usage

```sh
$ pip install cycloplanning
$ cycloplanning --help
Usage: cycloplanning [OPTIONS]

Options:
  -o, --output TEXT  file to write ICS to
  --url TEXT         URL to parse cycloplanning from
  --help             Show this message and exit.
```

## Contribute

```sh
$ curl -LsSf https://astral.sh/uv/install.sh | sh
$ git clone https://github.com/gma2th/cycloplanning-ics.git
$ cd cycloplanning-ics
$ uv sync
$ uv run cycloplanning -o cycloplanning.ics
$ uv run flask run
$ curl 127.0.0.1:5000/cycloplanning.ics
```
