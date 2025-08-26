def test_preview_output(markdown_output: str) -> None:
    """
    Validate that the preview output matches the expected Markdown formatting.

    Parameters:
        markdown_output (str): The expected Markdown-formatted output as a string.

    Returns:
        None
    """

    assert markdown_output.startswith("| Name | Age | City |")
