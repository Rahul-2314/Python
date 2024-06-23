import streamlit as st
import requests
from datetime import datetime, timedelta

# API key
api_key = "0501a6a860c04ef4883c3fc1a2aadc94"

# Streamlit GUI Topbar
st.title("Daily News App")
st.write("Get the latest news on your favorite topics!")

# CSS
st.markdown(
    """
    <style>
    .news-card {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
    }
    .news-title {
        color: lightgreen;
    }
    .article-number {
        color: lightpink;
        font-weight: bold;
    }
    .read-more {
        background-color: lightblue;
        font-weight: 800;
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
    }
    .read-more:hover {
        background-color: grey;
        color: black;
        text-decoration: none;
        transition: ease-in-out 0.3s;
    }
    #go-top {
        background-color: #4CAF50;
        color: white;
        font-weight: 800;
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
        position: fixed;
        bottom: 20px;
        right: 20px;
    }
    #go-top:hover {
        background-color: grey;
        color: black;
        text-decoration: none;
        transition: ease-in-out 0.3s;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Dropdown Popular Searches
popular_searches = ["All", "Cricket", "Movie", "Business",
                    "Technology", "Health", "Sports", "Entertainment"]
query = st.selectbox("Choose a topic:", popular_searches)

# search query
search_query = query

# Date input (last two days unavailable)
today = datetime.now()
two_days_ago = today - timedelta(days=2)
twenty_days_ago = today - timedelta(days=20)
default_date = two_days_ago
selected_date = st.date_input(
    "Choose a date", default_date, min_value=twenty_days_ago, max_value=two_days_ago)
formatted_date = selected_date.strftime("%Y-%m-%d")

if search_query:
    # endpoint url
    endpoint_url = f"https://newsapi.org/v2/everything?q={search_query}&from={formatted_date}&sortBy=publishedAt&apiKey={api_key}"

    try:
        # fetching response
        response = requests.get(endpoint_url)
        data = response.json()

        if data["status"] == "ok":
            contents = data["articles"]
            st.write(f"Total Results Found: {data['totalResults']}")

            for idx, content in enumerate(contents, start=1):
                title = content.get('title', '')
                content_text = content.get('content', '')

                if title and content_text and "[removed]" not in title:
                    st.markdown(
                        # HTML
                        f"""
                        <div class="news-card">
                            <h2 class="news-title"><span class="article-number">Article {idx}:</span> {title}</h2>
                            <h4>Source: {content['source']['name']}</h4>
                            <p>{content.get('description', 'No description available')}</p>
                            <a href="{content['url']}" target="_blank" class="read-more">Read more</a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            # "Go to Top" button
            st.markdown(
                """
                <a id="go-top" href="#daily-news-app">Go to Top</a>
                """,
                unsafe_allow_html=True
            )
        else:
            st.error("Error fetching news data")

    # handle exceptions
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
