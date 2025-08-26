import subprocess
import tempfile
from io import StringIO

import pytest

from mdtable import cli


def test_cli_help() -> None:
    """
    Test that the CLI help message is displayed correctly.

    Returns:
        None
    """
    result = subprocess.run(["mdtable", "--help"], capture_output=True, text=True)
    assert "Generate Markdown tables" in result.stdout


def test_cli_output(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Test the CLI output using monkeypatching.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Fixture for safely patching built-ins and environment during the test.

    Returns:
        None
    """
    # Create a temporary CSV file to simulate --input
    input_data = "Name,Age,City\nAlice,30,NYC\nBob,25,LA\nCharlie,35,Chicago\n"
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write(input_data)
        tmp.flush()

        # Simulate CLI args with --input and --preview
        monkeypatch.setattr("sys.argv", ["mdtable", "--input", tmp.name, "--preview"])

        # Capture stdout
        buffer = StringIO()
        monkeypatch.setattr("sys.stdout", buffer)

        cli.main()
        output = buffer.getvalue()

        assert "| Name    | Age | City    |" in output
        assert "| Alice   | 30  | NYC     |" in output
