# main.py

from modules.scraper import FinanceScraper
from modules.sentiment_analyzer import SentimentAnalyzer
import time

def main():
    # File paths
    input_file = 'data/input_headlines.txt'
    output_file = 'data/sentiment_output.txt'

    # Step 1: Scrape finance headlines and save to input file
    print("🔎 Starting Finance Scraper...")
    scraper = FinanceScraper(input_file_path=input_file)
    scraper.process()

    # Optional pause just to be safe — not always needed but useful for slow writes
    time.sleep(1)

    # Step 2: Analyze sentiments of the scraped headlines
    print("\n💬 Starting Sentiment Analysis...")
    analyzer = SentimentAnalyzer(input_file_path=input_file, output_file_path=output_file)
    analyzer.process()

    print("\n✅ Project 3 completed successfully!")

if __name__ == "__main__":
    main()
