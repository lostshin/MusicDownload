import re

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.youtube.com/results?search_query=pitbull")
content = request.content
soup = BeautifulSoup(content, "html.parser")
for element in soup.find_all('a',{"rel": "spf-prefetch"}):
    img_value = element.get('href').split("=")[1]
    all_img = soup.find_all('img',{"data-ytimg": True, "width":True, "alt":True, "height":True, "onload":True})
    img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value),str(all_img))).strip("[\"\']")
    video_img = img.replace("&amp;","&")
    print(video_img)
