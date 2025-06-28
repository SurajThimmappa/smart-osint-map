import requests

def fetch_news(keyword, api_key):
    url = f"https://gnews.io/api/v4/search?q={keyword}&lang=en&token={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['articles']
    else:
        print("Failed to fetch news:", response.status_code)
        return []
