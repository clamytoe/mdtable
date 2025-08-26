import pytest

from mdtable.core import generate_md_table


def test_generate_md_table(sample_table):
    result = generate_md_table(sample_table)
    assert "| Name | Age | City |" in result
    assert "| :--- | :--- | :--- |" in result
    assert "| Alice | 30 | NYC |" in result


@pytest.mark.parametrize(
    "alignment_inputs",
    ["center,right", "CENTER,RIGHT", ["center", "right"], ["CENTER", "RIGHT"]],
)
def test_alignment_formats(alignment_inputs):
    data = [["Name", "Age"], ["Alice", "30"]]
    result = generate_md_table(data, alignment_inputs)
    assert "| :---: | ---: |" in result
