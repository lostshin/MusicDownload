import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for time in soup.find_all('span',{"class":"video-time","aria-hidden":"true"}):
    print(time.text)