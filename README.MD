# 🕸️ CS325 Project 2 - Web Scraper for News Headlines

## Project Overview

This project implements a Python-based web scraper that fetches business headlines from multiple news websites using `requests` and `BeautifulSoup`. The script takes input URLs from a `urls.txt` file and writes all extracted headlines into a `headings.txt` file.

The main goals are:

- To understand web scraping basics
- To automate headline extraction
- To apply file input/output handling
- To deal with real-world HTTP response and parsing scenarios

---

## 📁 Project Structure

- `web_scraper.py` — The main scraping script
- `urls.txt` — List of news URLs to scrape
- `headings.txt` — Output file storing the extracted headlines
- `requirements.yml` — Conda environment file
- `README.md` — Project documentation

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/Rohoxoxo/CS325_project1.git
cd CS325_project1/project2_scraper
```

### 2. Create and Activate Conda Environment

Run the following:

```bash
conda env create -f requirements.yml
conda activate webscraping_env
```

### 3. Install Required Libraries

If not using Conda, you can install with pip:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Program

To start scraping:

```bash
python web_scraper.py
```

This script will:

- Read the list of URLs from `urls.txt`
- Scrape headlines from each site
- Save all headlines into `headings.txt`

---

## 📝 Prompts Used (Input URLs)

You can edit or replace the default URLs in the `urls.txt` file. Example:

```
https://www.denverpost.com/business/
https://www.forbes.com/business/
https://www.bbc.com/news/business
```

Make sure the URLs are from sites that allow scraping (i.e., don't block requests with 403 or 401 errors).

---

## 📄 Output Files

After running the script, a file named `headings.txt` is created or updated. It contains the headlines grouped by their source site:

```
### Headlines from https://www.bbc.com/news/business:
- Trump tariffs could be death knell for US-Africa trade pact
- Americans could pay more for everyday basics under Trump's new tariffs
- Commencement speech: The surprising pitfall of your passions
...
```

---

## 🧠 How It Works

- The script reads URLs from `urls.txt`
- For each URL, it:
  - Sends an HTTP GET request
  - Parses HTML using BeautifulSoup
  - Extracts text from `<h1>`, `<h2>`, `<h3>`, and `<title>` tags
  - Filters out short/empty text
  - Appends results to `headings.txt`

Duplicate headlines are automatically removed using Python’s `set()`.

---

## 🧪 Libraries Used

- `requests` — To fetch webpage data
- `beautifulsoup4` — For HTML parsing
- `os`, `set`, and basic file operations

---

## 👨‍💻 Author

**Name**: Rohit Chandel  
**Course**: CS325 — Spring 2025  
**Project**: Web Scraping for News Headlines (Project 2)
