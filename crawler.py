import requests
from bs4 import BeautifulSoup


def crawl_website(url, keyword):
    results = []

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        for para in paragraphs:
            text = para.get_text().strip()
            if keyword.lower() in text.lower():
                results.append(text)

    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results
