# Markdown Table Generator (*mdtable*)

> *An easy way to creating markdown tables from csv files.*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

NOTE: This project was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

## Initial setup

```zsh
cd Projects
git clone https://github.com/clamytoe/mdtable.git
cd mdtable
```

### Anaconda setup

If you are an Anaconda user, this command will get you up to speed with the base installation.

```zsh
conda env create
conda activate mdtable
```

### Regular Python setup

If you are just using normal Python, this will get you ready, but I highly recommend that you do this in a virtual environment.
There are many ways to do this, the simplest using *venv*.

```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Final setup

```zsh
pip install -e .
```

## Usage

```text
usage: mdtable [-h] --input INPUT [--output OUTPUT] [--align ALIGN] [--preview]

Generate Markdown tables from CSV

options:
  -h, --help       show this help message and exit
  --input INPUT    Path to CSV file
  --output OUTPUT  Path to save Markdown output
  --align ALIGN    Comma-separated alignment (e.g. left,center,right)
  --preview        Preview table in terminal
```

## Examples

For the following examples, I will be using the following data:

*xrp-rich.csv*

```csv
Percentage, # Accounts, Balance equals (or greater than)
0.01 %, 691, 6_692_587.586946 XRP
0.1 %, 6_910, 350_491.824569 XRP
0.2 %, 13_820, 197_695.303092 XRP
0.5 %, 34_549, 96_445.903096 XRP
1 %, 69_098, 50_025.789126 XRP
2 %, 138_197, 25_003.992913 XRP
3 %, 207_295, 15_642.899993 XRP
4 %, 276_394, 10_686.116118 XRP
5 %, 345_492, 8_370.264763 XRP
10 %, 690_984, 2_396.754360 XRP
```

### Example 1

```zsh
mdtable --input xrp-rich.csv --output output.md --align right,center,right
```

This will generate a markdown table from the data in `xrp-rich.csv` and save it to `output.md`. The alignments will be right,center, and right.

*output.md*

| Percentage |  # Accounts |  Balance equals (or greater than) |
| ---: | :---: | ---: |
| 0.01 % |  691 |  6,692,587.586946 XRP |
| 0.1 % |  6,910 |  350,491.824569 XRP |
| 0.2 % |  13,820 |  197,695.303092 XRP |
| 0.5 % |  34,549 |  96,445.903096 XRP |
| 1 % |  69,098 |  50,025.789126 XRP |
| 2 % |  138,197 |  25,003.992913 XRP |
| 3 % |  207,295 |  15,642.899993 XRP |
| 4 % |  276,394 |  10,686.116118 XRP |
| 5 % |  345,492 |  8,370.264763 XRP |
| 10 % |  690,984 |  2,396.754360 XRP |

### Example 2

```zsh
mdtable --input xrp-rich.csv --preview
```

This will generate a markdown table from the data in `xrp-rich.csv` and preview it in the terminal.

```text
+------------+-------------+-----------------------------------+
| Percentage |  # Accounts |  Balance equals (or greater than) |
+------------+-------------+-----------------------------------+
| Percentage |  # Accounts |  Balance equals (or greater than) |
| 0.01 %     |  691        |  6,692,587.586946 XRP             |
| 0.1 %      |  6,910      |  350,491.824569 XRP               |
| 0.2 %      |  13,820     |  197,695.303092 XRP               |
| 0.5 %      |  34,549     |  96,445.903096 XRP                |
| 1 %        |  69,098     |  50,025.789126 XRP                |
| 2 %        |  138,197    |  25,003.992913 XRP                |
| 3 %        |  207,295    |  15,642.899993 XRP                |
| 4 %        |  276,394    |  10,686.116118 XRP                |
| 5 %        |  345,492    |  8,370.264763 XRP                 |
| 10 %       |  690,984    |  2,396.754360 XRP                 |
+------------+-------------+-----------------------------------+
```

## Contributing

Contributions are welcomed.
Tests can be run with with `pytest -v`, please ensure that all tests are passing and that you've checked your code with the following packages before submitting a pull request:

* black
* flake8
* isort
* mypy
* pytest-cov

I am not adhering to them strictly, but try to clean up what's reasonable.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "mdtable" is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog

* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.13.3-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-0.1.0-blue.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/mdtable.svg
[issues-url]:https://github.com/clamytoe/mdtable/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/mdtable.svg
[fork-url]:https://github.com/clamytoe/mdtable/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/mdtable.svg
[stars-url]:https://github.com/clamytoe/mdtable/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/mdtable.svg
[license-url]:https://github.com/clamytoe/mdtable/blob/main/LICENSE
