import requests
import json

query = input("what type of news do you want? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-08-30&sortBy=publishedAt&apiKey=fcb59dd04a5046d6ae2320e47b2fcda5"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("_____________________________________________________")