# main.py
# This is the main controller script for Project 3.
# It connects both Project 2 (scraper) and Project 1 (sentiment analyzer),
# running them in sequence to automate the process from headline scraping to sentiment analysis.

from modules.scraper import FinanceScraper               # Import the scraper class from Project 2
from modules.sentiment_analyzer import SentimentAnalyzer # Import the sentiment analyzer from Project 1
import time                                               # Used to pause briefly if needed

def main():
    """
    Main function that runs the full news sentiment pipeline:
    1. Scrapes finance headlines from a news site
    2. Saves them to a file
    3. Analyzes the sentiment of each headline
    4. Writes the sentiment results to another file
    """

    # Define paths to the input and output files
    input_file = 'data/input_headlines.txt'       # Headlines will be saved here
    output_file = 'data/sentiment_output.txt'     # Sentiment results will be saved here

    # STEP 1: Scrape news headlines
    print("🔎 Starting Finance Scraper...")
    scraper = FinanceScraper(input_file_path=input_file)  # Create a scraper object
    scraper.process()                                     # Scrape and save headlines

    # Optional short pause to ensure file writing is complete before analysis starts
    time.sleep(1)

    # STEP 2: Analyze the sentiments of the scraped headlines
    print("\n💬 Starting Sentiment Analysis...")
    analyzer = SentimentAnalyzer(input_file_path=input_file, output_file_path=output_file)
    analyzer.process()  # Analyze each headline and save the results

    # Final message after both steps complete successfully
    print("\n✅ Project 3 completed successfully!")

# Run the main function when this script is executed
if __name__ == "__main__":
    main()
