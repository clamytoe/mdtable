def test_preview_output(markdown_output):
    assert markdown_output.startswith("| Name | Age | City |")
