import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to retrieve news articles from a news API
def retrieve_articles(api_key, stock_symbol):
    url = f"https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json()["articles"]
    return articles

# Function to perform sentiment analysis on a given text
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    sentiment = sentiment_scores["compound"]
    return sentiment

# Set your API key
api_key = "5c009057e8bc460d80924a8f0948967b"

# Get user input for stock market choice
print("Available Stock Markets:")
print("1. American Stock Market (US)")
print("2. Australian Stock Market (AU)")
print("3. Japanese Stock Market (JP)")

market_choice = input("Select a stock market (enter the corresponding number): ")

# Set the appropriate stock market symbol based on user input
if market_choice == "1":
    stock_market = "US"
elif market_choice == "2":
    stock_market = "AU"
elif market_choice == "3":
    stock_market = "JP"
else:
    print("Invalid choice. Exiting the program.")
    exit()

# Retrieve available stocks in the selected stock market
url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=9VMnMVl6isbtAT0P2n7sYu6qpSxgssDQ"  # Replace with your API endpoint or data source
response = requests.get(url)
available_stocks = response.json()

# Display the available stocks
print("Available Stocks:")
for stock in available_stocks:
    print(stock)

# Get user input for the desired stock symbol
stock_symbol = input("Enter the stock symbol you want to retrieve news articles for: ")

# Retrieve news articles for the selected stock symbol
articles = retrieve_articles(api_key, stock_symbol)

# Perform sentiment analysis on the headlines and descriptions of the retrieved articles
for article in articles:
    headline = article["title"]
    description = article["description"]

    headline_sentiment = analyze_sentiment(headline)
    description_sentiment = analyze_sentiment(description)

    print("Headline:", headline)
    print("Sentiment:", headline_sentiment)

    print("Description:", description)
    print("Sentiment:", description_sentiment)
    print("-------------------")
