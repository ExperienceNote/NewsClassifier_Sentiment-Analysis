import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
#url = "https://news.google.com/news/headlines/section/q/world%20sports%20news/world%20sports%20news?ned=in&hl=en-IN&gl=IN"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

links = soup.find_all("a",{"class":"nuEeue hzdq5d ME7ew"})

for link in links:
    print(link.text)
