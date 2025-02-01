### The main file for the project
# import modules.news_getter as news_getter
# import modules.news_summarizer as news_summarizer
from modules import news_getter, news_summarizer

import streamlit as st


newsGetter = news_getter.NewsGetter()
tech_articles = newsGetter.get_tech_articles()

# Données JSON
articles = news_summarizer.summarize_news(tech_articles["results"])



# Configuration de l'interface Streamlit
st.title("Articles en cartes")

# Affichage des articles sous forme de cartes
for article in articles:
    with st.container():
        st.subheader(article["article_title"])
        st.write(f"**Source :** {article['article_source']}")
        st.write(article["summary_msg"])
        st.divider()
