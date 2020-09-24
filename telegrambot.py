import datetime
from datetime import date

import telebot
from telebot import types

import details
import parse_university
import parser
import jsonparser
import utils

URL_CONST = 'https://ruz.spbstu.ru'
file = open('text.txt', 'r')
bot = telebot.TeleBot(file.readline())
URL_GROUP = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, студент.")
    change_group(message)


@bot.message_handler(commands=['help'])
def help_fun(message):
    bot.send_message(message.chat.id, "Все команды:\n"
                                      "/help - выводит все доступные функции\n"
                                      "/check_week - просмотр всей недели\n"
                                      "/check_today - просмотр расписания на сегодня\n"
                                      "/check_date - просмотр конкретной даты\n"
                                      "/check_tomorrow - просмотр расписания на завтра\n"
                                      "/check_on_this_time-просмотр пары которая ближе всего по времени\n"
                                      "/change_group-изменить группу\n"
                                      "/get_on_your_device - скачать расписание в ваш календарь")


@bot.message_handler(commands=['check_week'])
def check_week(message):
    url = jsonparser.get_json(int(message.chat.id))
    if not url:
        bot.send_message(message.chat.id, 'Простите, но сначала нужно записать вашу группу. Для этого нажмине /change_group')
        return
    list_lessons = parser.parse_week(url=url)
    if not list_lessons:
        bot.send_message(message.chat.id, "Нет расписания на эту неделю.")
        return
    all_text = 'On this week:'
    for day in list_lessons:
        all_text += '\n\nDay:' + day['day'] + "\n"
        for i in range(0, len(day['subjects'])):
            all_text += 'Время: ' + day['time'][i] + '\n\t'
            all_text += 'Предмет: ' + day['subjects'][i] + '\n\t'
            all_text += 'Вид занятия: ' + day['type_lesson'][i] + '\n\t'
            all_text += 'Преподаватель: ' + day['teacher'][i] + '\n\t'
            all_text += 'Место проведение: ' + day['place'][i] + '\n\n'
    bot.send_message(message.chat.id, all_text)


@bot.message_handler(commands=['check_today'])
def check_this_day(message, date_t=date.today()):
    url = jsonparser.get_json(int(message.chat.id))
    if not url:
        bot.send_message(message.chat.id,
                         'Простите, но сначала нужно записать вашу группу. Для этого нажмине /change_group')
        return
    list_lessons = parser.parse_week(url=url)
    if not list_lessons:
        bot.send_message(message.chat.id, "На этой неделе нет занятий. Можно флексить.")
        return
    this_day = details.check_date(list_with_date=list_lessons, date_t=date_t)
    if not this_day:
        bot.send_message(message.chat.id, "Нет пар. Можно спокойно отдыхать.")
        return
    all_text = 'Дата: (' + this_day['day'] + ')\n\t'
    for i in range(0, len(this_day['subjects'])):
        all_text += 'Время: ' + this_day['time'][i] + '\n\t'
        all_text += 'Предмет: ' + this_day['subjects'][i] + '\n\t'
        all_text += 'Вид занятия: ' + this_day['type_lesson'][i] + '\n\t'
        all_text += 'Преподаватель: ' + this_day['teacher'][i] + '\n\t'
        all_text += 'Место проведение: ' + this_day['place'][i] + '\n\n'
    bot.send_message(message.chat.id, all_text)


@bot.message_handler(commands=['check_date'])
def check_date(message):
    bot.send_message(message.chat.id, 'Пожалуйста введите дату того дня, расписания которого хотите увидеть в формате '
                                      'например 20.09.2020.')
    bot.register_next_step_handler(message, find_date_timetable)


def find_date_timetable(message):
    date_str = utils.checkDate(message.text)
    if not date_str:
        bot.send_message(message.chat.id, "Поставьте пожалуйста нормальную дату")
        check_date(message)
        return
    date_t = details.find_week(date_str)
    url = jsonparser.get_json(int(message.chat.id))
    if not url:
        bot.send_message(message.chat.id,
                         'Простите, но сначала нужно записать вашу группу. Для этого нажмине /change_group')
        return
    list_lessons = parser.parse_week(url + '?date=' + str(date_t.year) + '-' + str(date_t.month) + '-' + str(date_t.day))
    if not list_lessons:
        bot.send_message(message.chat.id, "На этой неделе нет занятий. Можно флексить.")
        return
    days, mouth, year = message.text.split('.')
    day_t = datetime.datetime(year=int(year), month=int(mouth), day=int(days))
    this_day = details.check_date(list_with_date=list_lessons, date_t=day_t)
    if not this_day:
        bot.send_message(message.chat.id, "Нет пар. Можно спокойно отдыхать.")
        return
    all_text = 'Дата: (' + this_day['day'] + ')\n\t'
    for i in range(0, len(this_day['subjects'])):
        all_text += 'Время: ' + this_day['time'][i] + '\n\t'
        all_text += 'Предмет: ' + this_day['subjects'][i] + '\n\t'
        all_text += 'Вид занятия: ' + this_day['type_lesson'][i] + '\n\t'
        all_text += 'Преподаватель: ' + this_day['teacher'][i] + '\n\t'
        all_text += 'Место проведение: ' + this_day['place'][i] + '\n\n'
    bot.send_message(message.chat.id, all_text)


@bot.message_handler(commands=['check_tomorrow'])
def check_tomorrow(message):
    date_t = datetime.datetime(date.today().year, date.today().month, date.today().day)
    print(date_t)
    date_t += datetime.timedelta(days=1)
    print(date_t)
    check_this_day(message, date_t=date_t)


@bot.message_handler(commands=['check_on_this_time'])
def check_on_this_time(message):
    url = jsonparser.get_json(int(message.chat.id))
    if not url:
        bot.send_message(message.chat.id,
                         'Простите, но сначала нужно записать вашу группу. Для этого нажмине /change_group')
        return
    list_lessons = parser.parse_week(url=url)
    if not list_lessons:
        bot.send_message(message.chat.id, "На этой неделе нет занятий. Можно флексить.")
        return
    this_day = details.check_date(list_with_date=list_lessons, date_t=date.today())
    if not this_day:
        bot.send_message(message.chat.id, "Сегодня нет пар, можете флексить спокойно.")
        return
    this_time_index = details.check_time(list_lessons=this_day)
    if not this_time_index:
        bot.send_message(message.chat.id, "На сегодня пар уже не будет")
        return
    all_text = 'Дата: (' + this_day['day'] + ')\n\t'
    all_text += 'Время: ' + this_day['time'][this_time_index] + '\n\t'
    all_text += 'Предмет: ' + this_day['subjects'][this_time_index] + '\n\t'
    all_text += 'Вид занятия: ' + this_day['type_lesson'][this_time_index] + '\n\t'
    all_text += 'Преподаватель: ' + this_day['teacher'][this_time_index] + '\n\t'
    all_text += 'Место проведение: ' + this_day['place'][this_time_index] + '\n\n'
    bot.send_message(message.chat.id, all_text)


@bot.message_handler(commands=['change_group'])
def change_group(message):
    university = parse_university.parse_university()
    markup = types.InlineKeyboardMarkup(row_width=4)
    for univ in university:
        item = types.InlineKeyboardButton(univ['university_name'], callback_data=univ['university_href'])
        markup.add(item)
    bot.send_message(message.chat.id, "Пожалуйста, выберите ваш факультет", reply_markup=markup)


@bot.message_handler(commands=['get_on_your_device'])
def get_on_device(message):
    url = jsonparser.get_json(int(message.chat.id))
    if not url:
        bot.send_message(message.chat.id,
                         'Простите, но сначала нужно записать вашу группу. Для этого нажмине /change_group')
        return
    bot.send_message(message.chat.id, "Следующая ссылка будет ссылкой для скачивания расписанию на эту неделю")
    bot.send_message(message.chat.id, URL_CONST + parser.get_href_on_load(url))


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
    if message.text.lower() == 'россия':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAICSV9rWsew_xyjF_zPz1w3S1TR5AT1AAJfCQACeVziCZCAjXmZR2L6GwQ')


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    global URL_GROUP
    URL_GROUP = URL_CONST + call.data
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="Please, insert your group",
                          reply_markup=None)

    bot.register_next_step_handler(message=call.message, callback=callback_registration)


def callback_registration(message):
    group = utils.checkGroup(message.text)
    if not group:
        bot.send_message(message.chat.id, "Введите группу коректно")
        change_group(message)
        return 
    global URL_GROUP
    list_group = parse_university.parse_group(URL_GROUP)
    for elem in list_group:
        if elem['group'] == group:
            URL_GROUP = URL_CONST + elem['href']
    jsonparser.post_json(user_id=int(message.chat.id), url=URL_GROUP)
    bot.send_message(message.chat.id, URL_GROUP)
    bot.send_message(message.chat.id, "Теперь можно просматривать ваше расписание. Пожалуйста, нажмите /help")


bot.polling(none_stop=True)
