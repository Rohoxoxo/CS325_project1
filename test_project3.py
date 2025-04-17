# test_project3.py

from modules.sentiment_analyzer import SentimentAnalyzer
from modules.scraper import FinanceScraper

# Test that sentiment analyzer correctly labels a positive headline
def test_sentiment_positive():
    analyzer = SentimentAnalyzer("dummy.txt", "dummy_out.txt")
    sentiment = analyzer.analyze_sentiment("The stock market jumped today with big gains.")
    assert sentiment == "Positive"

# Test that scraper returns a list (even if it's empty due to connection)
def test_scraper_returns_list():
    scraper = FinanceScraper("dummy_input.txt")
    result = scraper.scrape_headlines("https://www.denverpost.com/business/")
    assert isinstance(result, list)
