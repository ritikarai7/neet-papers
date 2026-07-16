# NEET Previous Year Papers

This repository contains NEET previous year question papers collected using Python web scraping.

## Features

- Scrapes NEET previous year question paper details.
- Stores data in CSV format.
- Includes paper year, paper name, and download links.
- Easy to update when new papers are added.

## Technologies Used

- Python
- Requests
- BeautifulSoup (bs4)
- Pandas
- CSV

## Project Structure

```
neet-papers/
│
├── neet_papers.py
├── neet_papers.csv
├── README.md
```

## CSV Fields

The CSV file contains:

- Year
- Paper Name
- PDF Link
- Solution Link (if available)
- Download Link

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

3. Run the script:

```bash
python neet_papers.py
```

## Output

The script generates a CSV file containing the details of NEET previous year question papers.

## Disclaimer

This project is intended for educational and learning purposes only. The data belongs to their respective source websites.
