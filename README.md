# 🧠 CS325 Project 3 - Integrated News Sentiment Analyzer

## 📌 Project Overview

This project brings together **Project 1 (Sentiment Analysis)** and **Project 2 (News Headline Scraper)** into a **fully automated pipeline**.

It scrapes **real financial news headlines** from the web, analyzes their **sentiment** (Positive, Negative, or Neutral), and stores the results in an output file.

The key goals are:

- ✅ Combine scraping + sentiment model logic
- ✅ Use Object-Oriented Programming (OOP)
- ✅ Write test cases using `pytest`
- ✅ Modularize everything into clean Python classes and files

---

## 📁 Project Structure

```
PROJECT 3/
├── data/
│   ├── input_headlines.txt       # Headlines scraped from the web
│   └── sentiment_output.txt      # Sentiment results for each headline
│
├── modules/
│   ├── scraper.py                # Scrapes finance headlines (Project 2 logic)
│   ├── sentiment_analyzer.py     # Classifies headline sentiment (Project 1 logic)
│   └── base_model.py             # Base class inherited by both scraper & analyzer
│
├── main.py                       # Runs the full pipeline (scrape → analyze)
├── test_project3.py              # Pytest file with test cases
├── environment.yaml              # Conda environment file
├── .gitignore                    # Files and folders to exclude from git
└── README.md                     # This file
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/CS325_project3.git
cd CS325_project3
```

### 2. Create and Activate Conda Environment

```bash
conda env create -f environment.yaml
conda activate project3_env
```

> ⚠️ Make sure your environment includes `requests`, `beautifulsoup4`, `pytest`, and any model libraries (like `transformers` or `torch` if you upgrade your sentiment model).

---

## 🚀 How to Run the Program

Just one command:

```bash
python main.py
```

This will:

1. Scrape **real-time financial headlines** from Yahoo Finance (or a similar source)
2. Save them in `data/input_headlines.txt`
3. Analyze the sentiment of each headline
4. Save the sentiments in `data/sentiment_output.txt`

---

## 💬 Example Input & Output

### 📥 `input_headlines.txt` (scraped)

```
Tesla stock jumps 12% after earnings beat
Amazon to lay off 10,000 workers
Investors cautious as inflation reports loom
```

### 📤 `sentiment_output.txt` (analyzed)

```
Positive
Negative
Neutral
```

---

## 🧪 How to Run Tests

Test file: `test_project3.py`

Run this command:

```bash
pytest test_project3.py
```

This will run:

- ✅ A test for correct sentiment analysis
- ✅ A test to confirm the scraper returns headline data

---

## 🔧 How It Works (Beginner-Friendly Flow)

1. **main.py** controls the pipeline.
2. It first creates a `FinanceScraper` object:
   - This grabs headlines from the web and writes them to `input_headlines.txt`.
3. Then it creates a `SentimentAnalyzer` object:
   - It reads those headlines and analyzes them using simple keyword rules (or your model).
   - The output goes to `sentiment_output.txt`.

All file handling, data reading/writing, and logic are done using **Python classes with inheritance** from a common `BaseModel`.

---

## 🧱 Object-Oriented Concepts Used

- ✅ **Modules** — Organized by functionality (`scraper`, `analyzer`, `base_model`)
- ✅ **Classes** — Each file defines its own class
- ✅ **Inheritance** — All core classes inherit from a common `BaseModel`
- ✅ **Method overriding** — `process()` is overridden in each class for customized behavior

---

## 📄 Files You Can Ignore

Your `.gitignore` should contain:

```
__pycache__/
*.pyc
.venv/
data/*.txt  # Optional if you don't want to track local scraped/output files
```

---

## 📚 Dependencies

Listed in `environment.yaml`. Main libraries include:

- `requests`
- `beautifulsoup4`
- `pytest`
- _(optional)_ `transformers`, `torch` (if using LLM)

---

## 👨‍💻 Author

**Name**: Rohit Chandel  
**Course**: CS325 — Spring 2025  
**Project**: Integrated News Sentiment Analyzer (Project 3)

---

Let me know if you want the **`.gitignore`** next or if you're ready to push everything to GitHub for final submission ✅
