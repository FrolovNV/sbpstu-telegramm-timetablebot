import requests
from bs4 import BeautifulSoup

TEMPLATE_URL = 'https://ruz.spbstu.ru'
URL = 'https://ruz.spbstu.ru/faculty/95/groups/29899'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
    , 'accept': '*/*'}


def get_html(url, params=None):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='schedule__day')
    days = []
    switcher_link = soup.find_all('a', class_='switcher__link')
    print(switcher_link[2]['href'])
    for item in items:
        days.append(item.find('div', class_='schedule__date').get_text())
    print(days)
    lessons = []
    i: int = 0
    for item in items:
        daylis = {'day': days[i], 'lesson': []}
        for les in item.find_all('li', class_="lesson"):
            lesson = les.find('div', class_='lesson__subject')
            time = lesson.find('span', class_='lesson__time')
            lessons_params = les.find('div', class_='lesson__params')
            type_lesson = lessons_params.find('div', class_='lesson__type').get_text()
            lessons_teacher = lessons_params.find('div', class_='lesson__teachers')
            if lessons_teacher:
                lessons_teacher = lessons_teacher.get_text()
            else:
                lessons_teacher = "Преподаватель не указан "
            lessons_place = lessons_params.find('div', class_='lesson__places').get_text()
            print(time.contents[0].get_text(), end='-')
            print(time.contents[2].get_text(), end=' ')
            print(lesson.contents[2].get_text(), end=' ')
            print(type_lesson, end=' ')
            print(lessons_teacher, end=' ')
            print(lessons_place)
        lessons.append(daylis)


def parse():
    url = URL
    while True:
        html = get_html(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        if soup.find('li', class_='schedule__empty'):
            break
        if html.status_code == 200:
            get_content(html.text)
            url = TEMPLATE_URL + soup.find_all('a', class_='switcher__link')[2]['href']
        else:
            print("Something come wrong\n")
            break


def parse_week(url):
    html = get_html(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    class_day = soup.find_all('li', class_='schedule__day')
    if not class_day:
        return None
    days_date = soup.find_all('div', class_='schedule__date')
    lessons_on_week = []
    i: int = 0
    for item in class_day:
        day = {'day': days_date[i].get_text(), 'subjects': [], 'time': [], 'type_lesson': [], 'teacher': [], 'place': []}
        for lesson in item.find_all('li', class_='lesson'):
            subject = lesson.find('div', class_='lesson__subject')
            time = subject.find('span', class_='lesson__time')
            lessons_params = lesson.find('div', class_='lesson__params')
            type_lesson = lessons_params.find('div', class_='lesson__type').get_text()
            lessons_teacher = lessons_params.find('div', class_='lesson__teachers')
            if lessons_teacher:
                lessons_teacher = lessons_teacher.get_text()
            else:
                lessons_teacher = "Преподаватель не указан "
            lessons_place = lessons_params.find('div', class_='lesson__places').get_text()
            time = str(time.contents[0].get_text()) + '-' + str(time.contents[2].get_text())
            day['time'].append(time)
            day['subjects'].append(subject.contents[2].get_text())
            day['type_lesson'].append(type_lesson)
            day['teacher'].append(lessons_teacher)
            day['place'].append(lessons_place)
        lessons_on_week.append(day)
        i += 1
    return lessons_on_week


def get_href_on_load(url):
    html = get_html(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    href_ = soup.find('div', class_= "d-none d-sm-none d-md-block col-md-6")
    return href_.contents[1]['href']


get_href_on_load("https://ruz.spbstu.ru/faculty/95/groups/29899")