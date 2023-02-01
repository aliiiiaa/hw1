from pprint import pprint
import requests
from bs4 import BeautifulSoup
import random


URL = 'https://rezka.ag/animation/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',

}

def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    anime = []
    for item in items:
        anime.append({
            'Title': item.find('div', class_='b-content__inline_item-link').find('a').get_text,
            'Link': item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            'Description': item.find('div', class_='b-content__inline_item-link').find('div').string,
            'Info': item.find('span', class_='info').string if item.find('span', class_='info')
                                                               is not None else 'полнометражное аниме'
        })
        return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 3):
            html = get_html(f'{URL}page/{page}/')
            current = get_data(html.text)
            answer.extend(current)
        return answer
    else:
        raise Exception('Error')

parser()




