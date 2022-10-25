from pprint import pprint
from bs4 import BeautifulSoup
import requests

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


# We should import this class in the main file
class Scraper:
    def __init__(self, URL: str):
        self.__url = URL
        self.soup = self.get_soup(URL)

    @property
    def URL(self) -> str:
        return self.__url

    @URL.setter
    def URL(self, new_url: str):
        self.__url = new_url
        self.soup = self.get_soup(new_url)

    @staticmethod
    def get_soup(url: str):
        response = requests.get(url, headers=HEADERS)
        return BeautifulSoup(response.content, 'html.parser')

    def get_google_result(self):
        articles = self.soup.select('a:has(h3)')
        # for article in articles:
        #     href = article['href']
        #     text = article.h3.get_text(strip=True)
        #     print(text, href)

        return {article.h3.get_text(strip=True): article['href'] for article in articles}


def test():
    scraper = Scraper('https://www.google.com/search?q=cat')
    result = scraper.get_google_result()
    pprint(result)


# This bit won't run when we import this file from another file
if __name__ == "__main__":
    test()
