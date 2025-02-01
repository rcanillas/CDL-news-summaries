import requests
from newspaper import Article
from modules import news_getter, news_summarizer

test_url = "https://www.thenews.com.pk/latest/1278449-a-city-killer-asteroid-might-hit-earth-how-worried-should-we-be"

def get_article_content(article_url:str):

    try : 
        article = Article(article_url)
        article.download()
        article.parse()
        content = article.text
    except Exception as e:
        print(f"Unexpected error: {e}")
        content = "Full content is not available."
         
    return content

if __name__ == "__main__":
        newsGetter = news_getter.NewsGetter()
        tech_articles = newsGetter.get_tech_articles()

        for news_item in tech_articles["results"]:
                print(get_article_content(news_item["link"]))

                