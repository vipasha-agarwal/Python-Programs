import requests
from bs4 import BeautifulSoup
url = "https://jsonplaceholder.typicode.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1
# }
# headers= {
#     'Content-type': 'application/json; charset = UTF-8',
# }
# response = requests.post(url, headers=headers, json = data )
# print(response.text)