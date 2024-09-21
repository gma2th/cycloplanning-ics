from pathlib import Path
import pytest

FIXTURE_PATH = "tests/fixture"


@pytest.fixture
def cycloplanning_html():
    with open(Path(FIXTURE_PATH) / "cycloplanning.html") as f:
        content = f.read()
    return content
