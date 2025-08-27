import csv
import sys

ALIGN_MAP = {
    "left": ":---",
    "center": ":---:",
    "right": "---:",
}
VALID_ALIGNMENTS = {"left", "center", "right"}


def format_commas(cell: str) -> str:
    """
    Replace underscores with commas in numeric strings.

    Parameters:
        cell (str): A string cell from the table.

    Returns:
        str: The formatted cell with underscores replaced by commas.
    """
    return cell.replace("_", ",")


def generate_md_table(
    data: list[list[str]], alignments: str | list[str] | None = None
) -> str:
    """
    Generate a Markdown-formatted table from a list of rows.

    Parameters:
        data (List[List[str]]): A list of rows, where each row is a list of string
        cells.
        alignments (Optional[Union[List[str], str]]): Column alignments ('left',
        'center', 'right') as a list or comma-separated string.

    Returns:
        str: The generated Markdown table as a string.
    """
    if not data:
        raise ValueError("Table data is empty.")
    elif not all(len(row) == len(data[0]) for row in data[1:]):
        raise ValueError("All rows must have the same number of columns.")

    headers = data[0]
    rows = data[1:]
    num_cols = len(headers)

    # Parse alignments
    if alignments:
        align_list = normalize_alignments(alignments)
        align_row = [ALIGN_MAP.get(a, ":---") for a in align_list]
    else:
        align_row = [":---"] * num_cols

    formatted_rows = [[format_commas(cell) for cell in row] for row in rows]

    # Build table
    table = ["| " + " | ".join(headers) + " |"]
    table.append("| " + " | ".join(align_row) + " |")
    for row in formatted_rows:
        padded_row = row + [""] * (num_cols - len(row))  # pad if row is short
        table.append("| " + " | ".join(padded_row) + " |")

    return "\n".join(table)


def normalize_alignments(alignments: str | list[str]) -> list[str]:
    """
    Normalize alignment input into a lowercase list of alignment values.

    Parameters:
        alignments (Union[str, List[str]]): Alignment input as a comma-separated string
        or list of strings.

    Returns:
        List[str]: Normalized list of alignment values in lowercase.
    """
    if isinstance(alignments, str):
        alignments = alignments.split(",")
    normalized = [a.strip().lower() for a in alignments]
    for a in normalized:
        if a not in VALID_ALIGNMENTS:
            raise ValueError(f"Invalid alignment: '{a}'")
    return normalized


def read_csv(input_path: str = "") -> list[list[str]]:
    """
    Read a CSV file and return its contents as a list of rows.

    Parameters:
        input_path (str): Path to the input CSV file. If set to "-", reads from stdin.

    Returns:
        list[list[str]]: A list of rows, where each row is a list of string cells.
    """
    if input_path == "-":
        return list(csv.reader(sys.stdin))
    else:
        with open(input_path, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))


def write_output(output_path: str, content: str) -> None:
    """
    Write content to a file or stdout.

    Parameters:
        output_path (str): Path to the output file. If '-', content is written to
        stdout.
        content (str): The content to write.
    """
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(content)
