# Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application

import requests

#api key
api_key=f"0501a6a860c04ef4883c3fc1a2aadc94"

#query search
query=input("what type of news are you interested in? :")

#url
endpoint_url=f"https://newsapi.org/v2/everything?q={query}&from=2023-07-17&sortBy=publishedAt&apiKey=0501a6a860c04ef4883c3fc1a2aadc94"

try:
    response=requests.get(endpoint_url)
    data=response.json()
    print(f"\nTotal Results Found :{data['totalResults']}")
    print("="*30)

    if data["status"]=="ok":
        contents=data["articles"]
        for idx,content in enumerate(contents,start=1):
            print(f"Article {idx}:")
            print(f"Title: {content['title']}")
            print(f"Source: {content['source']['name']}")
            print(f"Description: {content['description']}")
            print(f"URL: {content['url']}")
            print(f"Content : {content['content']}")
            print("-" * 40)

    else:
        print("Error fetching news data")

except requests.exceptions.RequestException as e:
    print(f"An error occured :{e}")
