from tools.web_scraper import search_web, scrape_url
from tools.url_loader import load_content_from_url

class SearchAgent:
    def __init__(self):
        pass
        
    def search_and_scrape(self, sub_tasks):
        """
        Performs search and scraping for the given sub-tasks.
        Returns a combined string of all gathered text.
        """
        all_text = ""
        visited_urls = set()
        
        for task in sub_tasks:
            print(f"Searching for: {task}")
            results = search_web(task, max_results=3)
            
            for result in results:
                url = result.get('href')
                if url and url not in visited_urls:
                    print(f"Scraping: {url}")
                    content = load_content_from_url(url)
                    if content:
                        all_text += f"\n\nSource: {url}\n{content}"
                        visited_urls.add(url)
                        
        return all_text

if __name__ == "__main__":
    searcher = SearchAgent()
    # print(searcher.search_and_scrape(["Quantum Computing basics"]))
