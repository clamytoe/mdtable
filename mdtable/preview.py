from .core import format_commas


# Format row
def fmt_row(col_widths: list[int], num_cols: int, row: list[str]) -> str:
    """
    Format a row of cells for a Markdown-style table.

    Parameters:
        col_widths (List[int]): Widths for each column.
        num_cols (int): Total number of columns to format.
        row (List[str]): A list of string cells.

    Returns:
        str: The formatted row as a string.
    """
    padded = [
        row[i].ljust(col_widths[i]) if i < len(row) else " " * col_widths[i]
        for i in range(num_cols)
    ]
    return "| " + " | ".join(padded) + " |"


# Build horizontal line
def hr(col_widths: list[int]) -> str:
    """
    Build a horizontal line for a Markdown-style table.

    Parameters:
        col_widths (List[int]): A list of column widths.

    Returns:
        str: The formatted horizontal line as a string.
    """
    return "+" + "+".join(["-" * (w + 2) for w in col_widths]) + "+"


def preview_table(
    data: list[list[str]], alignments: str | list[str] | None = None
) -> None:
    """
    Render a Markdown-style table preview in the terminal.

    Parameters:
        data (List[List[str]]): A list of rows, where each row is a list of string
        cells.
        alignments (Optional[Union[List[str], str]]): Column alignments ('left',
        'center', 'right') as a list or comma-separated string.

    Returns:
        None
    """
    headers = data[0]
    rows = data[1:]
    num_cols = len(headers)

    # Determine column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < num_cols:
                col_widths[i] = max(col_widths[i], len(cell))

    formatted_data = [[format_commas(cell) for cell in row] for row in data]

    # Assemble preview
    lines = [hr(col_widths), fmt_row(col_widths, num_cols, headers), hr(col_widths)]
    for row in formatted_data:
        lines.append(fmt_row(col_widths, num_cols, row))
    lines.append(hr(col_widths))

    print("\n".join(lines))
