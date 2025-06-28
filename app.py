import streamlit as st
import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium
from news_fetcher import fetch_news
from config import NEWS_API_KEY


# --- Setup Streamlit UI ---
st.set_page_config(layout="wide")
st.title("🛰️ Smart OSINT Map - Reddit Intel Feed (Live)")
st.markdown("Using Reddit API for live OSINT post extraction.")
st.subheader("📰 News Articles")

# --- Keyword input ---
keyword = st.text_input("🔍 Enter a keyword to search Reddit posts:", "Ukraine")

news_results = fetch_news(keyword, NEWS_API_KEY)

if news_results:
    for article in news_results:
        st.markdown(f"**{article['title']}**")
        st.write(article['description'])
        st.markdown(f"[Read more]({article['url']})\n")
        st.markdown("---")
else:
    st.warning("No news articles found.")

# --- Setup Reddit API ---
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# --- Fetch posts ---
def fetch_reddit_posts(keyword):
    results = []
    try:
        for submission in reddit.subreddit("all").search(keyword, limit=10, sort='new'):
            results.append({
                "title": submission.title,
                "url": submission.url,
                "subreddit": submission.subreddit.display_name,
                "author": str(submission.author),
                "created_utc": submission.created_utc
            })
    except Exception as e:
        st.error(f"Reddit API error: {e}")
    return results

# Location extractor
def extract_location(title):
    geolocator = Nominatim(user_agent="osint-map")
    try:
        location = geolocator.geocode(title, timeout=10)
        if location:
            return location.latitude, location.longitude, location.address
    except:
        pass
    return None, None, None
# --- UI Button ---
if st.button("📥 Fetch Reddit Posts"):
    with st.spinner("Collecting OSINT data from Reddit..."):
        posts = fetch_reddit_posts(keyword)
        if posts:
            st.success(f"Fetched {len(posts)} posts.")
            for i, post in enumerate(posts, 1):
                 lat, lon, address = extract_location(post["title"])
            if lat and lon:
                if "map" not in locals():
                    map = folium.Map(location=[lat, lon], zoom_start=2)
                folium.Marker(
                    [lat, lon],
                    popup=f"<b>{post['title']}</b><br><a href='{post['url']}'>Open</a>",
                    tooltip=address,
                ).add_to(map)
                
                
                st.markdown(f"**{i}. [{post['title']}]({post['url']})**")
                st.caption(f"📆 Created | 🌐 r/{post['subreddit']} | 👤 u/{post['author']}")
                st.write("---")
        else:
            st.warning("No posts found.")

if "map" in locals():
    st.markdown("### 🗺️ Mapped OSINT Data")
    st_folium(map, width=700)
else:
    st.info("No mappable locations found in titles.")