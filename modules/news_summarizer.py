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
            {"article_id": news_item["article_id"], "summary_msg": summary_msg}
        )
    return summary_list


if __name__ == "__main__":
    news_articles_exemple = {
        "nextPage": "1738378824597020914",
        "results": [
            {
                "ai_org": "ONLY AVAILABLE IN CORPORATE PLANS",
                "ai_region": "ONLY AVAILABLE IN CORPORATE PLANS",
                "ai_tag": "ONLY AVAILABLE IN PROFESSIONAL AND CORPORATE PLANS",
                "article_id": "286150f6bcc6fc8476e35700a7cafff4",
                "category": ["technology"],
                "content": "ONLY AVAILABLE IN PAID PLANS",
                "country": ["united states of america"],
                "creator": ["By The Associated Press"],
                "description": "HAMDEN, Conn. (AP) — Amarri Monroe had 27 points "
                "in Quinnipiac's 81-69 win over Fairfield on "
                "Friday night.",
                "duplicate": True,
                "image_url": None,
                "keywords": None,
                "language": "english",
                "link": "https://www.dailyrecordnews.com/ap_news/sports/amarri-monroes-27-points-as-quinnipiac-tops-fairfield-81-69/article_dc21ce40-2152-50f9-894e-f1ad3d76083b.html",
                "pubDate": "2025-02-01 03:07:10",
                "pubDateTZ": "UTC",
                "sentiment": "ONLY AVAILABLE IN PROFESSIONAL AND CORPORATE PLANS",
                "sentiment_stats": "ONLY AVAILABLE IN PROFESSIONAL AND CORPORATE "
                "PLANS",
                "source_icon": "https://i.bytvi.com/domain_icons/dailyrecordnews.jpg",
                "source_id": "dailyrecordnews",
                "source_name": "Dailyrecordnews",
                "source_priority": 113511,
                "source_url": "https://www.dailyrecordnews.com",
                "title": "Amarri Monroe's 27 points as Quinnipiac tops Fairfield "
                "81-69",
                "video_url": None,
            },
            {
                "ai_org": "ONLY AVAILABLE IN CORPORATE PLANS",
                "ai_region": "ONLY AVAILABLE IN CORPORATE PLANS",
                "ai_tag": "ONLY AVAILABLE IN PROFESSIONAL AND CORPORATE PLANS",
                "article_id": "2d2ab275b11a07f88eb8887194c949fa",
                "category": ["technology"],
                "content": "ONLY AVAILABLE IN PAID PLANS",
                "country": ["united states of america"],
                "creator": ["", "Paul Tassi, Senior Contributor"],
                "description": "Looking for help with today's NYT Mini Crossword "
                "puzzle? Here are some hints and answers for the "
                "puzzle.",
                "duplicate": False,
                "image_url": "https://imageio.forbes.com/specials-images/imageserve/66a443f5e74a26761c258a2c/0x0.jpg?width=960",
                "keywords": [
                    "/gaming",
                    "/innovation",
                    "games",
                    "gaming",
                    "standard",
                    "innovation",
                ],
                "language": "english",
                "link": "https://www.forbes.com/sites/paultassi/2025/01/31/todays-nyt-mini-crossword-clues-and-answers-for-saturday-february-1/",
                "pubDate": "2025-02-01 03:06:20",
                "pubDateTZ": "UTC",
                "sentiment": "ONLY AVAILABLE IN PROFESSIONAL AND CORPORATE PLANS",
                "sentiment_stats": "ONLY AVAILABLE IN PROFESSIONAL AND CORPORATE "
                "PLANS",
                "source_icon": "https://i.bytvi.com/domain_icons/forbes.png",
                "source_id": "forbes",
                "source_name": "Forbes",
                "source_priority": 154,
                "source_url": "https://www.forbes.com",
                "title": "Today’s NYT Mini Crossword Clues And Answers For "
                "Saturday, February 1",
                "video_url": None,
            },
        ],
        "status": "success",
        "totalResults": 5197,
    }
    news_summarized = summarize_news(news_articles_exemple["results"])
    pprint(news_summarized)
