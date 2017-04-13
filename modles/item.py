import re

import requests
import youtube_dl
from bs4 import BeautifulSoup


def find_search_content(search):
    request = requests.get("https://www.youtube.com/results?search_query={}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup

def find_page_content(search):
    request = requests.get("https://www.youtube.com/results?{}".format(search))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup


def find_video(soup, all_item, i=1):
    for element in soup.find_all('a', {"rel": "spf-prefetch"}):
        video_title = element.get('title')
        video_link = element.get('href')
        img_value = element.get('href').split("=")[1]
        all_img = soup.find_all('img', {"alt": True, "width": True, "height": True, "onload": True, "data-ytimg": True})
        img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))).strip("[\"\' ] ")
        video_img = img.replace("&", "&")
        all_item['{}'.format(i)] = {"title": video_title, "link": "https://www.youtube.com{}".format(video_link),
                                    "img": video_img}
        i = i + 1
    return all_item


def video_time(soup, all_item, i=1):
    for time in soup.find_all('span', {"class": "video-time", "aria-hidden": "true"}):
        all_item.get('{}'.format(i))['time'] = time.text
        i = i + 1
    return all_item


def every_video(soup):
    all_item= {}  #一開始先宣告區域變數
    find_video(soup, all_item,i=1) #<---假如裡面又宣告一次
    video_time(soup, all_item,i=1) #對video_time來說~就沒有all_item這變數了所以才會錯誤!
    return all_item

def page_bar(soup):
    page = {}
    for page_value in soup.find_all('a', {"class": True, "data-visibility-tracking": True, "data-sessionlink": True,
                                          "aria-label": True}):
        page['{}'.format(page_value.text)] = page_value.get('href')

    return page


def download_mp3(url):
    ydl_opts = {'format': 'bestaudio/best', 'outtmpl': 'video/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_mp4(url):
    ydl_opts = {'format': 'best', 'outtmpl': 'video/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
