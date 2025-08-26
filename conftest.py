# tests/conftest.py
from io import StringIO

import pytest

from mdtable.core import generate_md_table


@pytest.fixture
def sample_table():
    return [
        ["Name", "Age", "City"],
        ["Alice", "30", "NYC"],
        ["Bob", "25", "LA"],
        ["Charlie", "35", "Chicago"],
    ]


@pytest.fixture
def markdown_output(sample_table):
    return generate_md_table(sample_table)


@pytest.fixture
def malformed_table():
    return [
        ["Name", "Age"],
        ["Alice", "30", "NYC"],  # Extra column
        ["Bob"],  # Missing column
    ]


@pytest.fixture
def cli_args(monkeypatch):
    def _inject(args):
        monkeypatch.setattr("sys.argv", ["mdtable"] + args)

    return _inject


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = StringIO()
    monkeypatch.setattr("sys.stdout", buffer)
    return buffer
