import requests
from bs4 import BeautifulSoup


def scrape_website(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    print("Status Code:", response.status_code)

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = soup.title.text if soup.title else ""

    paragraphs = soup.find_all("p")

    content = " ".join(
        [p.get_text(strip=True) for p in paragraphs[:20]]
    )

    return {
        "title": title,
        "content": content
    }