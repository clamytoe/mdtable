from io import StringIO
from typing import Callable

import pytest

from mdtable.core import generate_md_table


@pytest.fixture
def sample_table() -> list[list[str]]:
    """
    Provide a sample table fixture for testing Markdown table formatting.

    Returns:
        List[List[str]]: A list of rows, where each row is a list of string cells.
    """
    return [
        ["Name", "Age", "City"],
        ["Alice", "30", "NYC"],
        ["Bob", "25", "LA"],
        ["Charlie", "35", "Chicago"],
    ]


@pytest.fixture
def markdown_output(sample_table: list[list[str]]) -> str:
    """
    Generate the expected Markdown-formatted output for a sample table.

    Parameters:
        sample_table (List[List[str]]): A list of rows, where each row is a list of string cells.

    Returns:
        str: The expected Markdown output as a string.
    """
    return generate_md_table(sample_table)


@pytest.fixture
def malformed_table() -> list[list[str]]:
    """
    Provide a malformed table fixture for testing error handling and formatting edge cases.

    Returns:
        List[List[str]]: A list of rows, where each row is a list of string cells.
    """
    return [
        ["Name", "Age"],
        ["Alice", "30", "NYC"],  # Extra column
        ["Bob"],  # Missing column
    ]


@pytest.fixture
def cli_args(monkeypatch: pytest.MonkeyPatch) -> Callable:
    """
    Provide a helper function to inject CLI arguments using monkeypatching.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Fixture for safely patching built-ins and environment during the test.

    Returns:
        Callable: A function that sets sys.argv to simulate CLI input.
    """

    def _inject(args):
        monkeypatch.setattr("sys.argv", ["mdtable"] + args)

    return _inject


@pytest.fixture
def capture_stdout(monkeypatch: pytest.MonkeyPatch) -> StringIO:
    """
    Provide a fixture to capture stdout output during tests using monkeypatching.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Fixture for safely patching built-ins and environment during the test.

    Returns:
        StringIO: A StringIO object that captures printed output from sys.stdout.
    """

    buffer = StringIO()
    monkeypatch.setattr("sys.stdout", buffer)
    return buffer
