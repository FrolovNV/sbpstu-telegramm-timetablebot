import time
import re


def checkDate(date):
    try:
        new_date = ''
        for char in date:
            if char != ' ' and (char.isdigit() or char == '.'):
                new_date += char

        time.strptime(new_date, '%d.%m.%Y')
        return new_date
    except:
        return False


def checkGroup(num):
    new_num = ''
    for char in num:
        if char != ' ' and (char.isdigit() or char == '/'):
            new_num += char
    match = re.fullmatch(r'\d{7}\/\d{5}', new_num)
    return new_num if match else False
