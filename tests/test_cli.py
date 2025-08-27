import subprocess
import sys
import tempfile
from io import StringIO
from pathlib import Path

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
        monkeypatch (pytest.MonkeyPatch): Fixture for safely patching built-ins and
        environment during the test.

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


def test_cli_print(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Simulates CLI output by monkeypatching built-in functions.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Pytest fixture used to override built-ins
        like `print` or `sys.stdout` during the test.

    Returns:
        None
    """
    csv_content = "Percentage,# Accounts,Balance\n0.01 %,691,6_692_587.586946 XRP"
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".csv", delete=False
    ) as temp_csv:
        temp_csv.write(csv_content)
        temp_csv.flush()

        monkeypatch.setattr(sys, "argv", ["mdtable", "--input", temp_csv.name])
        captured = StringIO()
        monkeypatch.setattr(sys, "stdout", captured)

        try:
            cli.main()
        except SystemExit:
            pass

        output = captured.getvalue()
        assert "6,692,587.586946 XRP" in output


def test_cli_output_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """
    Simulates CLI output and writes to a temporary file using monkeypatching.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Fixture used to override built-ins
        like `print` or `sys.stdout` during the test.
        tmp_path (Path): Pytest fixture providing a temporary directory as a
        pathlib.Path object.

    Returns:
        None
    """
    csv_file = tmp_path / "input.csv"
    csv_file.write_text("Percentage,# Accounts,Balance\n0.1 %,6910,350_491.824569 XRP")

    output_file = tmp_path / "output.md"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "mdtable",
            "--input",
            str(csv_file),
            "--output",
            str(output_file),
            "--align",
            "right,center,right",
        ],
    )

    try:
        cli.main()
    except SystemExit:
        pass

    assert output_file.exists()
    content = output_file.read_text()
    assert "350,491.824569 XRP" in content
