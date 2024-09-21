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
$ curl -sSf https://rye.astral.sh/get | bash
$ git clone https://github.com/gma2th/cycloplanning-ics.git
$ cd cycloplanning-ics
$ rye sync
$ rye run cycloplanning -o cycloplanning.ics
$ rye run flask run
$ curl 127.0.0.1:5000/cycloplanning.ics
```
