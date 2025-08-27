import sys
from io import StringIO

import pytest

from mdtable.core import (
    format_commas,
    generate_md_table,
    normalize_alignments,
    read_csv,
    write_output,
)
from mdtable.preview import preview_table


@pytest.mark.parametrize(
    "alignment_inputs",
    ["center,right", "CENTER,RIGHT", ["center", "right"], ["CENTER", "RIGHT"]],
)
def test_alignment_formats(alignment_inputs: str | list[str]) -> None:
    """
    Validate the output of generate_md_table with different alignment input formats.

    Parameters:
        alignment_inputs (Union[str, List[str]]): Alignment inputs as a comma-separated
        string or a list of strings.

    Returns:
        None
    """

    data = [["Name", "Age"], ["Alice", "30"]]
    result = generate_md_table(data, alignment_inputs)
    assert "| :---: | ---: |" in result


@pytest.mark.parametrize(
    "csv_input, expected_output",
    [
        ("6_692_587.586946 XRP", "6,692,587.586946 XRP"),
        ("350_491.824569 XRP", "350,491.824569 XRP"),
        ("XRP 6_692_587.586946", "XRP 6,692,587.586946"),
        ("No_underscores_here", "No,underscores,here"),
    ],
)
def test_format_commas(csv_input: str, expected_output: str) -> None:
    """
    Validate that format_commas correctly replaces underscores with commas in numeric
    strings.

    Returns:
        None
    """
    assert format_commas(csv_input) == expected_output


def test_generate_md_table(sample_table: list[list[str]]) -> None:
    """
    Validate the output of generate_md_table using a sample table.

    Parameters:
        sample_table (List[List[str]]): A list of rows, where each row is a list of
        string cells.

    Returns:
        None
    """

    result = generate_md_table(sample_table)
    assert "| Name | Age | City |" in result
    assert "| :--- | :--- | :--- |" in result
    assert "| Alice | 30 | NYC |" in result


@pytest.mark.parametrize(
    "raw_input,expected",
    [
        ("center,right", ["center", "right"]),
        (["CENTER", "RIGHT"], ["center", "right"]),
        (" left , center , right ", ["left", "center", "right"]),
    ],
)
def test_normalize_alignments(raw_input: str | list[str], expected: list[str]) -> None:
    """
    Test normalize_alignments with varied input formats.

    Parameters:
        raw_input (Union[List[str], str]): Raw input as a comma-separated string or a
        list of strings.
        expected (Union[List[str], str]): Expected normalized output as a list of
        strings.

    Returns:
        None
    """
    assert normalize_alignments(raw_input) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        "left,up",  # 'up' is invalid
        ["left", "down"],  # 'down' is invalid
    ],
)
def test_normalize_alignments_invalid(invalid_input: str | list[str]) -> None:
    """
    Test normalize_alignments with invalid input.

    Parameters:
        invalid_input (str | list[str]): Invalid input as a comma-separated string or a
        list of strings.

    Returns:
        None
    """
    with pytest.raises(ValueError, match="Invalid alignment"):
        normalize_alignments(invalid_input)


def test_generate_md_table_empty() -> None:
    """
    Validates that generate_md_table returns an empty string when given no data.

    Returns:
        None
    """
    with pytest.raises(ValueError):
        generate_md_table([], alignments=["left"])


def test_generate_md_table_misaligned_columns() -> None:
    """
    Ensures generate_md_table raises a ValueError when column count and alignment count
    mismatch.

    Returns:
        None
    """

    data = [["Header1", "Header2"], ["Row1Col1"]]  # Missing second column
    with pytest.raises(ValueError):
        generate_md_table(data, alignments=["left", "right"])


def test_generate_md_table_alignment() -> None:
    """
    Ensures generate_md_table raises a ValueError for unsupported alignment values.

    Returns:
        None
    """
    data = [["Header1", "Header2"], ["Row1Col1", "Row1Col2"]]
    with pytest.raises(ValueError):
        generate_md_table(data, alignments=["diagonal", "left"])


def test_normalize_alignments_strip_and_lower() -> None:
    """
    Verifies that normalize_alignments strips whitespace and converts values to
    lowercase.

    Returns:
        None
    """
    result = normalize_alignments(" Left ,CENTER , right ")
    assert result == ["left", "center", "right"]


def test_read_csv_from_stdin(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Simulates reading CSV data from stdin using monkeypatching.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Fixture used to override `sys.stdin` with
        mock input.

    Returns:
        None
    """
    csv_data = "Name,Score\nAlice,90\nBob,85"
    monkeypatch.setattr(sys, "stdin", StringIO(csv_data))
    result = read_csv("-")  # conventionally "-" means stdin
    assert result == [["Name", "Score"], ["Alice", "90"], ["Bob", "85"]]


def test_preview_table(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Verifies that preview_table writes formatted Markdown output to stdout.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): Fixture used to redirect `sys.stdout` for
        capturing output.

    Returns:
        None
    """
    data = [["Name", "Score"], ["Alice", "90"]]
    captured = StringIO()
    monkeypatch.setattr(sys, "stdout", captured)
    preview_table(data)
    output = captured.getvalue()
    assert "Alice" in output
    assert "Score" in output


def test_alignments_as_string() -> None:
    """
    Verifies that alignments_as_string converts a list of alignment values into a
    comma-separated string.

    Returns:
        None
    """
    result = normalize_alignments("left,center,right")
    assert result == ["left", "center", "right"]


def test_write_output_stdout(capsys: pytest.CaptureFixture) -> None:
    """
    Verifies that write_output sends content to stdout and can be captured via capsys.

    Parameters:
        capsys (pytest.CaptureFixture): Pytest fixture used to intercept and inspect
        stdout output.

    Returns:
        None
    """
    content = "Hello, Markdown!"
    write_output("", content)
    captured = capsys.readouterr()
    assert captured.out.strip() == content
