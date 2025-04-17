# modules/sentiment_analyzer.py

from modules.base_model import BaseModel

class SentimentAnalyzer(BaseModel):
    def __init__(self, input_file_path, output_file_path):
        super().__init__(input_file_path, output_file_path)

    def analyze_sentiment(self, text):
        # Very basic keyword-based sentiment logic
        positive_keywords = ['gain', 'bullish', 'up', 'rise', 'profit', 'jump', 'increase']
        negative_keywords = ['drop', 'fall', 'down', 'loss', 'bearish', 'cut', 'decline']

        text_lower = text.lower()

        if any(word in text_lower for word in positive_keywords):
            return 'Positive'
        elif any(word in text_lower for word in negative_keywords):
            return 'Negative'
        else:
            return 'Neutral'

    def process(self):
        print("Reading input headlines...")
        headlines = self.read_input_file()
        print("🔍 DEBUG: Number of headlines read:", len(headlines))
        print("🔍 DEBUG: Sample headlines:", headlines[:3])

        print("Analyzing sentiments...")
        sentiments = []
        for h in headlines:
            result = self.analyze_sentiment(h)
            print(f"Headline: {h} → Sentiment: {result}")
            sentiments.append(result)

        print("Writing output sentiments...")
        self.write_output_file(sentiments)
        print("✅ Done! Sentiments saved.")
