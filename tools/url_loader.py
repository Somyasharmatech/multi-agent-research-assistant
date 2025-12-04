from tools.web_scraper import scrape_url
from tools.pdf_reader import read_pdf
import requests
import io

def load_content_from_url(url):
    """
    Loads content from a URL, handling PDFs and regular web pages.
    """
    if url.lower().endswith('.pdf'):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            f = io.BytesIO(response.content)
            return read_pdf(f)
        except Exception as e:
            print(f"Error loading PDF from URL {url}: {e}")
            return ""
    else:
        return scrape_url(url)

if __name__ == "__main__":
    # Test
    print(load_content_from_url("https://example.com"))
