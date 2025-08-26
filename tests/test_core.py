import pytest

from mdtable.core import generate_md_table, normalize_alignments


@pytest.mark.parametrize(
    "alignment_inputs",
    ["center,right", "CENTER,RIGHT", ["center", "right"], ["CENTER", "RIGHT"]],
)
def test_alignment_formats(alignment_inputs: str | list[str]) -> None:
    """
    Validate the output of generate_md_table with different alignment input formats.

    Parameters:
        alignment_inputs (Union[str, List[str]]): Alignment inputs as a comma-separated string or a list of strings.

    Returns:
        None
    """

    data = [["Name", "Age"], ["Alice", "30"]]
    result = generate_md_table(data, alignment_inputs)
    assert "| :---: | ---: |" in result


def test_generate_md_table(sample_table: list[list[str]]) -> None:
    """
    Validate the output of generate_md_table using a sample table.

    Parameters:
        sample_table (List[List[str]]): A list of rows, where each row is a list of string cells.

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
        raw_input (Union[List[str], str]): Raw input as a comma-separated string or a list of strings.
        expected (Union[List[str], str]): Expected normalized output as a list of strings.

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
        invalid_input (str | list[str]): Invalid input as a comma-separated string or a list of strings.

    Returns:
        None
    """
    with pytest.raises(ValueError, match="Invalid alignment"):
        normalize_alignments(invalid_input)
