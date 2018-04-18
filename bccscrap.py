import requests
from bs4 import BeautifulSoup

url = "http://www.bbc.com/news"
#url = "http://www.bbc.com/news/technology"

#url = "file:///Users/uditmehra/Downloads/Home%20-%20BBC%20News.htm"
r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

links = soup.find_all("h3")

for link in links:
    print(link.text)
