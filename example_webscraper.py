import threading
import requests
from queue import Queue
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, base_url, max_threads=5):
        self.base_url = base_url
        self.max_threads = max_threads
        self.queue = Queue()
        self.results = []
        self.visited = set()

    def scrape_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else "No title"
        
        # Extract first paragraph
        first_p = soup.find('p')
        first_paragraph = first_p.text if first_p else "No paragraph found"
        
        # Extract links
        links = [urljoin(self.base_url, a['href']) for a in soup.find_all('a', href=True)]
        
        return {
            "url": url,
            "title": title,
            "first_paragraph": first_paragraph,
            "links": links
        }

    def worker(self):
        while True:
            url = self.queue.get()
            if url is None:
                break
            if url not in self.visited:
                self.visited.add(url)
                print(f"Scraping: {url}")
                page_data = self.scrape_page(url)
                self.results.append(page_data)
                for link in page_data["links"]:
                    if link.startswith(self.base_url) and link not in self.visited:
                        self.queue.put(link)
            self.queue.task_done()

    def run(self):
        self.queue.put(self.base_url)
        threads = []
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        self.queue.join()

        for _ in range(self.max_threads):
            self.queue.put(None)
        for t in threads:
            t.join()

        return self.results

if __name__ == "__main__":
    scraper = WebScraper("https://python.org", max_threads=50)
    results = scraper.run()
    print(f"Scraped {len(results)} pages")
    for page in results[:5]:
        print(f"URL: {page['url']}")
        print(f"Title: {page['title']}")
        print(f"First Paragraph: {page['first_paragraph'][:100]}...")  # Truncate for brevity
        print(f"Links found: {len(page['links'])}")
        print("---")