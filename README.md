# 🛰️ Smart OSINT Map - Conflict Zone Intelligence Feed

This is a live intelligence-gathering dashboard that fetches and displays conflict-related data using OSINT sources like **Reddit** and **News APIs**.

## 🔍 Features

- 🌐 Reddit post extraction by keyword (e.g., explosion, Ukraine, protest)
- 📰 News article scraping via News API
- 📍 Real-time OSINT feed for monitoring conflict zones
- ⚡ Streamlit-based interactive dashboard

## 🚀 Tech Stack

- Python 🐍
- Streamlit 📊
- PRAW (Reddit API)
- News API
- Folium (Mapping - upcoming)
- Geopy (Location parsing - upcoming)

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/SurajThimmappa/smart-osint-map.git
   cd smart-osint-map
2.Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows

3.Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

4.Configure your API keys in a secrets.py file:

python
Copy
Edit
# config.py
REDDIT_CLIENT_ID = 'your_client_id'
REDDIT_CLIENT_SECRET = 'your_client_secret'
REDDIT_USER_AGENT = 'your_user_agent'
NEWS_API_KEY = 'your_news_api_key'

5.Run the app:

bash
Copy
Edit
streamlit run app.py
📍 Planned Features
Live Geolocation Mapping

Twitter OSINT integration (if API access available)

Real-time alerts for keyword matches

Telegram Bot for automated notifications

🛡️ Disclaimer
This project is for educational and research purposes only. Always respect privacy laws and platform terms of service when using OSINT tools.

Built with ❤️ by Suraj - 2025


