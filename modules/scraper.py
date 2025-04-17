# modules/scraper.py
# This file defines the FinanceScraper class which is used to fetch financial news headlines
# from a live website and save them to a text file. It inherits from BaseModel for file handling.

import requests  # Used to make HTTP requests to websites
from bs4 import BeautifulSoup  # Used to parse HTML content from web pages
from modules.base_model import BaseModel  # Import the reusable base class for file handling

class FinanceScraper(BaseModel):
    def __init__(self, input_file_path):
        """
        Constructor for the FinanceScraper class.
        
        Parameters:
        - input_file_path (str): Path to the file where scraped headlines should be saved.

        Note: This class doesn't use output_file_path, so we pass None to the base class.
        """
        super().__init__(input_file_path, output_file_path=None)

    def scrape_headlines(self, url="https://www.denverpost.com/business/"):
        """
        Connects to the given URL and extracts visible headlines.

        Parameters:
        - url (str): The URL to scrape headlines from (default is The Denver Post Business section)

        Returns:
        - A list of cleaned headlines, sorted alphabetically.
        """
        print(f"\n🔍 Scraping headlines from: {url}")

        try:
            # Send an HTTP GET request to the given URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP errors (e.g., 404, 403)

            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            headlines = set()  # Use a set to avoid duplicate headlines

            # Loop through common headline tags and extract text content
            for tag in ['h1', 'h2', 'h3', 'title']:
                for element in soup.find_all(tag):
                    text = element.get_text(strip=True)
                    # Only include non-empty headlines with more than 5 characters
                    if text and len(text) > 5:
                        headlines.add(text)

            # If headlines are found, return them as a sorted list
            if headlines:
                print(f"✅ Found {len(headlines)} headlines.")
                return sorted(headlines)
            else:
                print("⚠️ No headlines found.")
                return []

        except requests.RequestException as e:
            # If there's an issue connecting to the site, show the error
            print(f"❌ Error fetching {url}: {e}")
            return []

    def process(self):
        """
        Overrides the process() method from BaseModel.

        This method:
        - Calls scrape_headlines() to get the latest news
        - Saves the headlines to the input file defined in input_file_path
        """
        # Call the scrape method to get headlines
        headlines = self.scrape_headlines()

        # Save headlines to file only if some were found
        if headlines:
            with open(self.input_file_path, 'w') as file:
                for line in headlines:
                    file.write(line + '\n')
            print(f"📝 Headlines saved to {self.input_file_path}")
        else:
            print("⚠️ No headlines to save.")
