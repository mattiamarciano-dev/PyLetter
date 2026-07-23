from dotenv import load_dotenv
from newsapi import NewsApiClient
from Categories import Categories
from Article import Article

load_dotenv()

class NewsGetter:
    API_KEY: str

    def __init__(self, key: str) -> None:
        self.API_KEY = key

    def get_news(self, cat: Categories) -> list[Article]:
        newsapi = NewsApiClient(api_key=self.API_KEY)
        articles = []
        top_headlines = newsapi.get_top_headlines(category=cat.value)

        for article in top_headlines['articles']:
            articles.append(Article(article['title'], article['author'], article['source']['name'], article['description'], article['url'], article['urlToImage']))

        return articles
