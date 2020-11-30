import time
from datetime import date
import re

def checkDate(inp):
    try:
        new_date = ''
        today = date.today()
        begin_str = '01.09.' + str(today.year)
        end_str = '30.06.' + str(today.year + 1)
        begin = time.strptime(begin_str, '%d.%m.%Y')
        end = time.strptime(end_str, '%d.%m.%Y')
        for char in inp:
            if char != ' ' and (char.isdigit() or char == '.'):
                new_date += char

        cur = time.strptime(new_date, '%d.%m.%Y')
        if begin <= cur <= end:
            return new_date
        return "Incorrect Date"
    except:
        return "Invalid date"


def checkGroup(num):
    new_num = ''
    for char in num:
        if char != ' ' and (char.isdigit() or char == '/'):
            new_num += char
    match = re.fullmatch(r'\d{7}\/\d{5}', new_num)
    return new_num if match else False
