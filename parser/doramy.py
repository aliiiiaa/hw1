from pprint import pprint
import requests
from bs4 import BeautifulSoup
import random

URL = 'https://doramy.club/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',

}

def get_html_(url):
    req = requests.get(url, headers=HEADERS)
    return req

def get_data_(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='post-home')
    for item in items:
        doramy = [{
            'Title': item.find('span').string,
            'Link': item.find('a').get('href'),
            'Status': item.find('div').string if item.find('div') is not None else 'pipets',
            'Real_name': item.find('em').string
        }]
    return doramy


def parser_():
    html = get_html_(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 10):
            html = get_html_(f'{URL}page/{page}')
            current = get_data_(html.text)
            answer.extend(current)
        return answer
    else:
        raise Exception('Error')

parser()

