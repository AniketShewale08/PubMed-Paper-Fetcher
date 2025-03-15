# PubMed Paper Fetcher

## Overview

The **PubMed Paper Fetcher** is a Python-based command-line tool designed to fetch research papers from PubMed and filter them based on authors' affiliations. It identifies papers authored by professionals from pharmaceutical or biotech companies and outputs the results in a CSV file or console.

## Features

- Fetch research papers from PubMed using a custom query.
- Filter papers authored by industry professionals (pharmaceutical/biotech companies).
- Output results as a CSV file or print to the console.
- Provides a command-line interface (CLI) for ease of use.

## Technologies Used

- Python 3.8+
- [Biopython](https://biopython.org/) for PubMed API integration
- [Typer](https://typer.tiangolo.com/) for CLI
- [Pandas](https://pandas.pydata.org/) for data handling and CSV output
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

### Prerequisites

- Python 3.8 or higher
- Poetry installed globally. Install it with:

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

### Steps to Install

1. Install dependencies:
   ```bash
   cd PubMedPaperFetche
   poetry install
   ```

2. Activate the Poetry shell:
   ```bash
   poetry shell
   ```

3. Install the CLI tool:
   ```bash
   poetry install
   ```

## Usage

### Command-Line Interface (CLI)

Run the tool using the following syntax:

```bash
poetry run pubmedfetcher "<your query>" [--file <filename.csv>] [--debug]
```

### Options

- `<your query>`: The search query for PubMed.
- `--debug` or `-d`: Enable debug mode for detailed logs.
- `--file <filename.csv>` or `-f <filename.csv>`: Save results to the specified CSV file. If omitted, results are printed to the console.

### Example Usage

1. Fetch papers and print results:
   ```bash
   poetry run pubmedfetcher "Cancer Drug Development"
   ```

2. Fetch papers and save results to `output.csv`:
   ```bash
   poetry run pubmedfetcher "AI in Healthcare" --file output.csv
   ```

3. Enable debug mode for troubleshooting:
   ```bash
   poetry run pubmedfetcher "Machine Learning in Pharma" --debug
   ```

## Code Structure

```
Pubmedfetcher
├── src
|   ├──pubmedfetcher
│     ├── paper_fetcher.py   # Fetches papers from PubMed API
│     ├── paper_filter.py    # Filters papers based on affiliations
│     └── main.py            # CLI implementation
├── poetry.lock
├── pyproject.toml        # Poetry configuration
└── README.md            # Project documentation
```

## How It Works

1. **Fetch Papers**: Uses Biopython's Entrez API to search and retrieve papers from PubMed.
2. **Filter Papers**: Identifies non-academic authors by checking if their affiliations contain company-related keywords (e.g., "pharma", "biotech").
3. **Output Results**: Outputs the filtered papers to the console or saves them as a CSV file.

## Output Format

The CSV output contains the following columns:

- **PubmedID**: Unique identifier for the paper.
- **Title**: Paper title.
- **Publication Date**: Date of publication.
- **Non-academic Author(s)**: Authors affiliated with companies.
- **Company Affiliation(s)**: Names of pharmaceutical/biotech companies.
- **Corresponding Author Email**: Email of the corresponding author (if available).

### Sample Output (CSV Format)

| PubmedID  | Title                      | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|-----------|----------------------------|------------------|------------------------|-------------------------|----------------------------|
| 12345678  | AI in Pharma Research      | 2023-07-15       | He T, Shi T, Huang K              | School of Pharmacy Inc.             | Het@pfizer.com         |
| 87654321  | ML in Drug Development    | 2023-06-20       | Di Stefano M, Piazza L             | Department of Pharmacy, University of Pisa, 56124 Pisa Labs             | piazzal@biogen.com       |

## Error Handling

- Handles network issues and API failures gracefully.
- Informs the user when no results are found.
- Provides debug mode for troubleshooting issues.

## Future Improvements

- **Enhance filtering criteria**: Use more robust heuristics for company identification.
- **Support additional output formats**: JSON, Excel.
- **Develop a web interface** for better user experience.

## Contribution

Contributions are welcome! Feel free to submit pull requests or raise issues.


## Contact

For questions, reach out to **Aniket Shewale** at [aniketshewale26@example.com](mailto:aniketshewale26@example.com).

---

Thank you for using PubMed Paper Fetcher!

