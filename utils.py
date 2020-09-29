import time
import datetime
import re


def checkDate(date):
    try:
        new_date = ''
        begin = time.strptime('01.09.2020', '%d.%m.%Y')
        end = time.strptime('31.05.2021', '%d.%m.%Y')
        for char in date:
            if char != ' ' and (char.isdigit() or char == '.'):
                new_date += char

        cur = time.strptime(new_date, '%d.%m.%Y')
        if end < cur < begin:
            return "Incorrect Date"
        return new_date
    except:
        print('Invalid date')
        return "Invalid date"


def checkGroup(num):
    new_num = ''
    for char in num:
        if char != ' ' and (char.isdigit() or char == '/'):
            new_num += char
    match = re.fullmatch(r'\d{7}\/\d{5}', new_num)
    return new_num if match else False


# print(checkDate('22.09.2020'))
# print(checkDate('24.06.2021'))