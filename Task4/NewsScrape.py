import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/news"

response = requests.get(url)

if response.status_code == 200:
    print("Website opened successfully\n")

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []

    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.get_text(" ", strip=True)

        if href and "/articleshow/" in href and text:
            if len(text) < 150 and text not in headlines:
                headlines.append(text)

    print("News Headlines:\n")

    for i, headline in enumerate(headlines[:20], 1):
        print(i, headline)

else:
    print("Unable to open the website")

