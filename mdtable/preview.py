def preview_table(data, alignments=None):
    headers = data[0]
    rows = data[1:]
    num_cols = len(headers)

    # Determine column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < num_cols:
                col_widths[i] = max(col_widths[i], len(cell))

    # Build horizontal line
    def hr():
        return "+" + "+".join(["-" * (w + 2) for w in col_widths]) + "+"

    # Format row
    def fmt_row(row):
        padded = [
            row[i].ljust(col_widths[i]) if i < len(row) else " " * col_widths[i]
            for i in range(num_cols)
        ]
        return "| " + " | ".join(padded) + " |"

    # Assemble preview
    lines = [hr(), fmt_row(headers), hr()]
    for row in rows:
        lines.append(fmt_row(row))
    lines.append(hr())

    print("\n".join(lines))
