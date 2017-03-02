import requests
from bs4 import BeautifulSoup


def firstVideoId(search_query):
    r = requests.get('https://www.youtube.com/results?search_query={}'.format(search_query))
    soup = BeautifulSoup(r.text, 'lxml')
    ol = soup.find('ol', class_="item-section")
    video_length = ol.find('span', class_="video-time").text
    video_id = soup.select('div[data-context-item-id]')[0].attrs['data-context-item-id']
    return video_id, video_length




