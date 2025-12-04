import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

def search_web(query, max_results=5):
    """
    Searches the web using DuckDuckGo and returns a list of results.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(r)
    return results

def scrape_url(url):
    """
    Scrapes the content of a given URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

if __name__ == "__main__":
    # Test
    print(search_web("Quantum Computing"))
    print(scrape_url("https://example.com"))
