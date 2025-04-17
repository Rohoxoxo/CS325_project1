# modules/sentiment_analyzer.py
# This file defines the SentimentAnalyzer class, which reads news headlines from a file,
# analyzes the sentiment of each (Positive, Negative, or Neutral), and writes the results to another file.

from modules.base_model import BaseModel  # Import the base class for file reading/writing

class SentimentAnalyzer(BaseModel):
    def __init__(self, input_file_path, output_file_path):
        """
        Constructor method for SentimentAnalyzer.

        Parameters:
        - input_file_path (str): The file path where the headlines are stored (input).
        - output_file_path (str): The file path where sentiment results will be saved (output).
        """
        super().__init__(input_file_path, output_file_path)

    def analyze_sentiment(self, text):
        """
        A simple rule-based sentiment analysis method.

        Parameters:
        - text (str): A news headline (single line of text)

        Returns:
        - A string label: 'Positive', 'Negative', or 'Neutral'
        
        The logic checks for specific keywords in the text to determine sentiment.
        """
        # Define lists of keywords associated with positive and negative sentiment
        positive_keywords = ['gain', 'bullish', 'up', 'rise', 'profit', 'jump', 'increase']
        negative_keywords = ['drop', 'fall', 'down', 'loss', 'bearish', 'cut', 'decline']

        # Convert the input text to lowercase for easier comparison
        text_lower = text.lower()

        # Check if any positive keyword exists in the text
        if any(word in text_lower for word in positive_keywords):
            return 'Positive'
        # Check if any negative keyword exists in the text
        elif any(word in text_lower for word in negative_keywords):
            return 'Negative'
        # If no match, return Neutral
        else:
            return 'Neutral'

    def process(self):
        """
        Overrides the process() method from BaseModel.

        This method:
        - Reads the scraped headlines from the input file
        - Analyzes the sentiment of each headline
        - Writes the corresponding sentiment labels to the output file
        """
        print("Reading input headlines...")
        headlines = self.read_input_file()  # Read input headlines from file

        print("🔍 DEBUG: Number of headlines read:", len(headlines))
        print("🔍 DEBUG: Sample headlines:", headlines[:3])

        print("Analyzing sentiments...")
        sentiments = []

        # Loop through each headline and analyze sentiment
        for h in headlines:
            result = self.analyze_sentiment(h)
            print(f"Headline: {h} → Sentiment: {result}")
            sentiments.append(result)

        print("Writing output sentiments...")
        self.write_output_file(sentiments)  # Save results to the output file
        print("✅ Done! Sentiments saved.")
