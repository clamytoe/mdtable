import csv
import sys

ALIGN_MAP = {
    "left": ":---",
    "center": ":---:",
    "right": "---:",
}


def read_csv(input_path):
    if input_path:
        with open(input_path, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))
    else:
        return list(csv.reader(sys.stdin))


def write_output(output_path, content):
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(content)


def generate_md_table(data, alignments=None):
    if not data:
        return ""

    headers = data[0]
    rows = data[1:]
    num_cols = len(headers)

    # Parse alignments
    if alignments:
        if isinstance(alignments, str):
            align_list = [a.strip().lower() for a in alignments.split(",")]
        elif isinstance(alignments, list):
            align_list = [a.strip().lower() for a in alignments]
        align_row = [ALIGN_MAP.get(a, ":---") for a in align_list]
    else:
        align_row = [":---"] * num_cols

    # Build table
    table = ["| " + " | ".join(headers) + " |"]
    table.append("| " + " | ".join(align_row) + " |")
    for row in rows:
        padded_row = row + [""] * (num_cols - len(row))  # pad if row is short
        table.append("| " + " | ".join(padded_row) + " |")

    return "\n".join(table)
