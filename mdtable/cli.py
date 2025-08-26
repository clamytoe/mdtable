#!/usr/bin/env python3
import argparse

from .core import generate_md_table, read_csv, write_output
from .preview import preview_table


def main() -> None:
    """
    Main entry point for the CLI utility.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Generate Markdown tables from CSV")
    parser.add_argument("--input", required=True, help="Path to CSV file")
    parser.add_argument("--output", help="Path to save Markdown output")
    parser.add_argument(
        "--align", help="Comma-separated alignment (e.g. left,center,right)"
    )
    parser.add_argument(
        "--preview", action="store_true", help="Preview table in terminal"
    )
    args = parser.parse_args()

    data = read_csv(args.input)
    alignments = args.align.split(",") if args.align else None
    md_table = generate_md_table(data, alignments)

    if args.preview:
        preview_table(data, alignments)
    elif args.output:
        write_output(args.output, md_table)
    else:
        print(md_table)
