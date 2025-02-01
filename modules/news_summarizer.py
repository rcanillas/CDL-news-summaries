from modules import news_getter

from openai import OpenAI
from pprint import pprint
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()


def summarize_news(news_list):
    summary_list = []
    for news_item in news_list:
        news_content = f"""Title: {news_item['title']}
        Short Content: {news_item['description']}
        Source: {news_item['source_name']}"""
        print(news_content)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an intern in an High School newspaper. You job is to summarize news articles for your fellow high school student. Go Bears !",
                },
                {
                    "role": "user",
                    "content": f"Here is there content of the news: {news_content}\n"
                    "Summarize the key points, and give only this summary.",
                },
            ],
        )
        summary_msg = completion.choices[0].message.content
        print(summary_msg)
        summary_list.append(
            {
                "article_source": news_item["source_name"],
                "article_title": news_item["title"],
                "article_id": news_item["article_id"],
                "summary_msg": summary_msg,
            }
        )
    return summary_list


if __name__ == "__main__":
    newsGetter = news_getter.NewsGetter()
    tech_articles = newsGetter.get_tech_articles()
    news_summarized = summarize_news(tech_articles["results"])
    pprint(news_summarized)
