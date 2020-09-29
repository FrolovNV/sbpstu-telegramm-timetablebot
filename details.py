import datetime
import parser


def check_date(list_with_date, date_t):
    if not list_with_date:
        return False
    new_list = {'months': [], 'day': []}
    for day in list_with_date:
        number_day = day['day'][0:day['day'].find(' ')]
        month = day['day'][day['day'].find(' ') + 1:day['day'].find('.')]
        if month == 'сент':
            month = 9
        elif month == 'окт':
            month = 10
        elif month == 'нояб':
            month = 11
        elif month == 'дек':
            month = 12
        elif month == 'янв':
            month = 1
        elif month == 'фев':
            month = 2
        elif month == 'мар':
            month = 3
        elif month == 'апр':
            month = 4
        elif month == 'май':
            month = 5
        elif month == 'июн':
            month = 6
        new_list['months'].append(month)
        new_list['day'].append(int(day['day'][0: day['day'].find(' ')]))
    if date_t.month in new_list['months'] and date_t.day in new_list['day']:
        for day in list_with_date:
            if int(day['day'][0:day['day'].find(' ')]) == date_t.day:
                return day
    return False


def check_time(list_lessons):
    time = datetime.datetime.now()
    for i in range(len(list_lessons['subjects'])):
        first_time = list_lessons['time'][i][0: list_lessons['time'][i].find('-')]
        second_time = list_lessons['time'][i][list_lessons['time'][i].find('-') + 1: len(list_lessons['time'][i])]
        h_f_time = first_time[0: first_time.find(':')]
        m_f_time = first_time[first_time.find(':') + 1: len(first_time)]
        timeB = time.replace(hour=int(h_f_time), minute=int(m_f_time))
        h_s_time = second_time[0: second_time.find(':')]
        m_s_time = second_time[second_time.find(':') + 1: len(second_time)]
        timeE = time.replace(hour=int(h_s_time), minute=int(m_s_time))
        if (timeB <= time <= timeE) or (time <= timeB):
            return i
    return "No more"


def find_week(day):
    days, mouth, year = day.split('.')
    day_t = datetime.datetime(year=int(year), month=int(mouth), day=int(days))
    day_t -= datetime.timedelta(days=day_t.weekday())
    return day_t


# list_lessons = {'subjects': [1, 3, 4, 5], 'time': ['10:00-11:30', '12:00-13:30', '14:00-15:30', '16:00-17:30']}
# print(check_time(list_lessons))