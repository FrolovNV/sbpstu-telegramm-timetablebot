import requests
from bs4 import BeautifulSoup

URL = 'https://ruz.spbstu.ru'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
    , 'accept': '*/*'}


def parse_university():
    html = requests.get(url=URL, headers=HEADERS)
    if html.status_code != 200:
        return None
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('a', class_='faculty-list__link')
    if not items:
        return None
    university = []
    for item in items:
        university.append({'university_name': item.get_text(), 'university_href': item['href']})
    return university


def parse_group(url):
    html = requests.get(url=url, headers=HEADERS)
    if html.status_code != 200:
        return None
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('a', class_='groups-list__link')
    if not items:
        return None
    groups = []
    for item in items:
        groups.append({'group': item.get_text(), 'href': item['href']})
    return groups