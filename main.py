### The main file for the project

import streamlit as st

# Données JSON
articles = [
    {
        "article_id": "286150f6bcc6fc8476e35700a7cafff4",
        "article_source": "Dailyrecordnews",
        "article_title": "Amarri Monroe's 27 points as Quinnipiac tops Fairfield 81-69",
        "summary_msg": "Quinnipiac secured an 81-69 victory over Fairfield, with Amarri Monroe leading the way by scoring 27 points.",
    },
    {
        "article_id": "2d2ab275b11a07f88eb8887194c949fa",
        "article_source": "Forbes",
        "article_title": "Today’s NYT Mini Crossword Clues And Answers For Saturday, February 1",
        "summary_msg": "The article provides hints and answers for the New York Times Mini Crossword puzzle for Saturday, February 1. It's a helpful guide for those looking for assistance with the puzzle.",
    },
]

# Configuration de l'interface Streamlit
st.title("Articles en cartes :joy:")

# Affichage des articles sous forme de cartes
for article in articles:
    with st.container():
        st.subheader(article["article_title"])
        st.write(f"**Source :** {article['article_source']}")
        st.write(article["summary_msg"])
        st.divider()
