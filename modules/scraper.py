# modules/scraper.py

import requests  # For sending HTTP requests to websites
from bs4 import BeautifulSoup  # For parsing HTML content
from modules.base_model import BaseModel  # Import the base class

class FinanceScraper(BaseModel):
    def __init__(self, input_file_path):
        """
        Initialize the FinanceScraper object.
        We only use input_file_path here to store scraped headlines.
        """
        super().__init__(input_file_path, output_file_path=None)

    def scrape_headlines(self, url="https://www.denverpost.com/business/"):
        """
        Scrapes headlines from the given finance URL.
        Returns a list of clean headlines.
        """
        print(f"\n🔍 Scraping headlines from: {url}")

        try:
            # Send HTTP GET request
            response = requests.get(url)
            response.raise_for_status()  # Raise error if site returns a bad status

            # Parse HTML using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            headlines = set()  # Use a set to avoid duplicates

            # Search for common headline tags
            for tag in ['h1', 'h2', 'h3', 'title']:
                for element in soup.find_all(tag):
                    text = element.get_text(strip=True)
                    if text and len(text) > 5:
                        headlines.add(text)

            if headlines:
                print(f"✅ Found {len(headlines)} headlines.")
                return sorted(headlines)
            else:
                print("⚠️ No headlines found.")
                return []

        except requests.RequestException as e:
            print(f"❌ Error fetching {url}: {e}")
            return []

    def process(self):
        """
        Main method that runs the scraper and saves headlines.
        This overrides the 'process' method from BaseModel.
        """
        # Use default Yahoo Finance URL
        headlines = self.scrape_headlines()

        if headlines:
            # Save scraped headlines to the input file
            with open(self.input_file_path, 'w') as file:
             for line in headlines:
              file.write(line + '\n')
        print(f"📝 Headlines saved to {self.input_file_path}")

        print(f"📝 Headlines saved to {self.input_file_path}")
        
        print("⚠️ No headlines to save.")
