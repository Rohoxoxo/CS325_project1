# Step 1: Define your finance keywords
FINANCE_KEYWORDS = [
    "stock", "market", "tariff", "finance", "business", "economy", "economic",
    "trade", "investment", "invest", "job", "jobs", "employment", "interest rate",
    "tax", "revenue", "bank", "mortgage", "inflation", "IPO", "layoff", "recession",
    "retail", "GDP", "startup", "funding", "earnings", "crypto", "bitcoin",
    "company", "merger", "acquisition", "CEO", "dow", "nasdaq", "s&p", "share", "price"
]

# Step 2: Helper function to check finance-related headlines
def is_finance_related(text):
    return any(keyword in text.lower() for keyword in FINANCE_KEYWORDS)

# Step 3: Modify scrape_headlines to filter only finance-related headlines
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    print(f"\nScraping headlines from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = set()
        for tag in ['h1', 'h2', 'h3', 'title']:
            for headline in soup.find_all(tag):
                text = headline.get_text(strip=True)
                if text and len(text) > 5 and is_finance_related(text):
                    headlines.add(text)

        if headlines:
            print(f"Found {len(headlines)} finance-related headlines")
            return headlines
        else:
            print(f"No finance-related headlines found for: {url}")
            return None

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Step 4: Your save_headlines() function can stay the same
def save_headlines(url, headlines):
    with open("headings.txt", "a") as f:
        f.write(f"\n### Headlines from {url}:\n")
        for headline in headlines:
            f.write(f"- {headline}\n")
        f.write("\n")
    print(f"Headlines saved from: {url}")

# Step 5: Main function to read urls.txt and trigger scraping

def main():
    try:
        with open("urls.txt", "r") as f:
            urls = f.read().splitlines()

        for url in urls:
            headlines = scrape_headlines(url)
            if headlines:
                save_headlines(url, headlines)

    except FileNotFoundError:
        print("Error: urls.txt file not found.")

if __name__ == "__main__":
    main()
