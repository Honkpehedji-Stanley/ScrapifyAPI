import requests
from bs4 import BeautifulSoup
from app.utils import clean_text

URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception("Failed to retrieve data from website.")

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    for quote_div in soup.find_all("div", class_="quote"):
        text = clean_text(quote_div.find("span", class_="text").get_text())
        author = clean_text(quote_div.find("small", class_="author").get_text())
        tags = [clean_text(tag.get_text()) for tag in quote_div.find_all("a", class_="tag")]

        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    return quotes_data
