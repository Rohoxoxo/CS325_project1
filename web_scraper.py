# web_scraper.py

# Import required libraries
import requests  # For sending HTTP requests to websites
from bs4 import BeautifulSoup  # For parsing HTML content

# Function to scrape headlines from a single URL
def scrape_headlines(url):
    print(f"\nScraping headlines from: {url}")

    try:
        # Send HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise error if status code is not 200

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Create a set to store unique headlines
        headlines = set()

        # Look for headlines in typical tags: h1, h2, h3, title
        for tag in ['h1', 'h2', 'h3', 'title']:
            for headline in soup.find_all(tag):
                text = headline.get_text(strip=True)

                # Basic filtering: skip empty and very short headlines
                if text and len(text) > 5:
                    headlines.add(text)

        # Return headlines if any were found
        if headlines:
            print(f"✅ Found {len(headlines)} headlines")
            return headlines
        else:
            print("⚠️ No headlines found.")
            return None

    # Handle HTTP or connection-related errors
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

# Function to save the scraped headlines to a text file
def save_headlines(url, headlines):
    with open("headings.txt", "a") as f:
        f.write(f"\n### Headlines from {url}:\n")
        for headline in sorted(headlines):
            f.write(f"- {headline}\n")
    print(f"📝 Headlines saved from: {url}")

# Main function that controls program flow
def main():
    try:
        # Load list of URLs from a text file
        with open("urls.txt", "r") as f:
            urls = f.read().splitlines()

        # Loop over each URL and perform scraping
        for url in urls:
            headlines = scrape_headlines(url)

            # Save the headlines if found
            if headlines:
                save_headlines(url, headlines)

    # If urls.txt is missing, show a warning
    except FileNotFoundError:
        print("❌ Error: 'urls.txt' file not found. Please create it with URLs to scrape.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
