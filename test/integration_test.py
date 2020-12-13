import unittest
from datetime import datetime, date, time
from app.details import *
from app.parse_university import *
from app.parser_content import *
from app.jsonparser import *
import random

class IntegrationTest(unittest.TestCase):
    def test_check_data(self):
        today = date.today()
        dayOfWeek = today.weekday()
        if dayOfWeek != 0:
            mon = date.today() - datetime.timedelta(days = dayOfWeek)
        else:
            mon = date.today()
    
        str_mon = mon.strftime('%Y-%m-%d')
        link = 'https://ruz.spbstu.ru/faculty/95/groups/29899?date=' + str_mon
        
        if mon.strftime('%m') == '01':
             month = 'янв'
        elif mon.strftime('%m') == '02':
            month = 'фев'
        elif mon.strftime('%m') == '03':
            month = 'мар'
        elif mon.strftime('%m') == '04':
            month = 'апр'
        elif mon.strftime('%m') == '05':
            month = 'май'
        elif mon.strftime('%m') == '06':
            month = 'июн'
        elif mon.strftime('%m') == '09':
            month = 'cен'
        elif mon.strftime('%m') == '10':
            month = 'окт'
        elif mon.strftime('%m') == '11':
            month = 'нояб'
        elif mon.strftime('%m') == '12':
            month = 'дек'
        
        str_day = mon.strftime('%d') + ' ' + month + '., ' + 'пн'
        
        day_0 = {
            'day': str_day,
            'subjects': ['Архитектура программных систем', 'Теория вероятностей и математическая статистика', 'Микропроцессорные системы', 'Базы данных'],
            'time': ['10:00-11:40', '12:00-13:40', '14:00-15:40', '18:00-19:40'],
            'type_lesson': ['Лекции', 'Лекции', 'Лекции', 'Лекции'],
            'teacher': [' Дробинцев Дмитрий Федорович', ' Семенов Константин Константинович', ' Круглов Сергей Константинович', ' Вишневская Татьяна Александровна'],
            'place': ['DL,  ауд. Дистанционно', 'DL,  ауд. Дистанционно', 'DL,  ауд. Дистанционно', 'DL,  ауд. Дистанционно']
            }   
        
        lessons_on_week = parse_week(link)
        self.assertEqual(check_data(lessons_on_week, date.today()), day_0)
        
        day_1 = {
            'day': '16 нояб., пн',
            'subjects': ['Архитектура программных систем', 'Теория вероятностей и математическая статистика', 'Микропроцессорные системы', 'Базы данных'],
            'time': ['10:00-11:40', '12:00-13:40', '14:00-15:40', '18:00-19:40'],
            'type_lesson': ['Лекции', 'Лекции', 'Лекции', 'Лекции'],
            'teacher': [' Дробинцев Дмитрий Федорович', ' Семенов Константин Константинович', ' Круглов Сергей Константинович', ' Вишневская Татьяна Александровна'],
            'place': ['DL,  ауд. Дистанционно', 'DL,  ауд. Дистанционно', 'DL,  ауд. Дистанционно', 'DL,  ауд. Дистанционно']
            } 
		
        old_date = datetime.date(2020, 11, 16)
        lessons_on_week = parse_week('https://ruz.spbstu.ru/faculty/95/groups/29899?date=2020-11-16')
        self.assertEqual(check_data(lessons_on_week, old_date), day_1)
        
        day_2 = {
            'day': '24 нояб., вт',
            'subjects': ['Военная подготовка'],
            'time': ['08:30-17:20'],
            'type_lesson': ['Практика'],
            'teacher': ['Преподаватель не указан '],
            'place': ['Военная кафедра,  ауд. кафедра']
        } 
        lessons_on_week = parse_week('https://ruz.spbstu.ru/faculty/95/groups/29899?date=2020-11-23')
        new_date = datetime.date(2020, 11, 24)
        self.assertEqual(check_data(lessons_on_week, new_date), day_2)
     
     
    def test_post_json(self):
        link = 'https://ruz.spbstu.ru/faculty/95/groups'
        n = random.randint(0, 500)
        self.assertEqual(post_json(n, link), True)
        self.assertEqual(post_json('6', link), True)
     
     
    def test_get_json(self):
        url = 'https://ruz.spbstu.ru/faculty/95/groups'
        self.assertEqual(get_json(1), url)
        self.assertEqual(get_json('error'), False)
     
     
    def test_parse_group(self):
        groups = [{'group': '3530202/00001', 'href': '/faculty/95/groups/29807'},
                  {'group': '3530202/00002', 'href': '/faculty/95/groups/29808'},
                  {'group': '3530203/00001', 'href': '/faculty/95/groups/29823'},
                  {'group': '3530203/00002', 'href': '/faculty/95/groups/29824'},
                  {'group': '3530901/00001', 'href': '/faculty/95/groups/29828'},
                  {'group': '3530901/00002', 'href': '/faculty/95/groups/29829'},
                  {'group': '3530901/00003', 'href': '/faculty/95/groups/29830'},
                  {'group': '3530901/00004', 'href': '/faculty/95/groups/29831'},
                  {'group': '3530901/00005', 'href': '/faculty/95/groups/29832'},
                  {'group': '3530901/00006', 'href': '/faculty/95/groups/29833'},
                  {'group': '3530902/00001', 'href': '/faculty/95/groups/29809'},
                  {'group': '3530902/00002', 'href': '/faculty/95/groups/29810'},
                  {'group': '3530902/00003', 'href': '/faculty/95/groups/29811'},
                  {'group': '3530903/00001', 'href': '/faculty/95/groups/29825'},
                  {'group': '3530903/00002', 'href': '/faculty/95/groups/29826'},
                  {'group': '3530903/00003', 'href': '/faculty/95/groups/29827'},
                  {'group': '3530904/00001', 'href': '/faculty/95/groups/29812'},
                  {'group': '3530904/00002', 'href': '/faculty/95/groups/29813'},
                  {'group': '3530904/00003', 'href': '/faculty/95/groups/29814'},
                  {'group': '3530904/00004', 'href': '/faculty/95/groups/29815'},
                  {'group': '3530904/00005', 'href': '/faculty/95/groups/29816'},
                  {'group': '3530904/00006', 'href': '/faculty/95/groups/29817'},
                  {'group': '3532702/00001', 'href': '/faculty/95/groups/29818'},
                  {'group': '3532703/00001', 'href': '/faculty/95/groups/29819'},
                  {'group': '3532704/00001', 'href': '/faculty/95/groups/29821'},
                  {'group': '3532704/00002', 'href': '/faculty/95/groups/29822'},
                  {'group': '3532705/00001', 'href': '/faculty/95/groups/29820'},
                  {'group': '3530202/90001', 'href': '/faculty/95/groups/29859'},
                  {'group': '3530202/90002', 'href': '/faculty/95/groups/29860'},
                  {'group': '3530203/90001', 'href': '/faculty/95/groups/29861'},
                  {'group': '3530203/90002', 'href': '/faculty/95/groups/29862'},
                  {'group': '3530901/90001', 'href': '/faculty/95/groups/29877'},
                  {'group': '3530901/90002', 'href': '/faculty/95/groups/29878'},
                  {'group': '3530901/90003', 'href': '/faculty/95/groups/29879'},
                  {'group': '3530901/90004', 'href': '/faculty/95/groups/29880'},
                  {'group': '3530901/90005', 'href': '/faculty/95/groups/29881'},
                  {'group': '3530901/90006', 'href': '/faculty/95/groups/29882'},
                  {'group': '3530902/90001', 'href': '/faculty/95/groups/29863'},
                  {'group': '3530902/90002', 'href': '/faculty/95/groups/29864'},
                  {'group': '3530902/90003', 'href': '/faculty/95/groups/29865'},
                  {'group': '3530903/90001', 'href': '/faculty/95/groups/29883'},
                  {'group': '3530903/90002', 'href': '/faculty/95/groups/29884'},
                  {'group': '3530903/90003', 'href': '/faculty/95/groups/29885'},
                  {'group': '3530904/90001', 'href': '/faculty/95/groups/29866'},
                  {'group': '3530904/90002', 'href': '/faculty/95/groups/29867'},
                  {'group': '3530904/90003', 'href': '/faculty/95/groups/29868'},
                  {'group': '3530904/90004', 'href': '/faculty/95/groups/29869'},
                  {'group': '3530904/90005', 'href': '/faculty/95/groups/29870'},
                  {'group': '3530904/90006', 'href': '/faculty/95/groups/29871'},
                  {'group': '3532702/90001', 'href': '/faculty/95/groups/29872'},
                  {'group': '3532703/90001', 'href': '/faculty/95/groups/29873'},
                  {'group': '3532704/90001', 'href': '/faculty/95/groups/29875'},
                  {'group': '3532704/90002', 'href': '/faculty/95/groups/29876'},
                  {'group': '3532705/90001', 'href': '/faculty/95/groups/29874'},
                  {'group': '3530202/80201', 'href': '/faculty/95/groups/29891'},
                  {'group': '3530202/80202', 'href': '/faculty/95/groups/29892'},
                  {'group': '3530203/80101', 'href': '/faculty/95/groups/29893'},
                  {'group': '3530203/80102', 'href': '/faculty/95/groups/29894'},
                  {'group': '3530901/80101', 'href': '/faculty/95/groups/29907'},
                  {'group': '3530901/80201', 'href': '/faculty/95/groups/29908'},
                  {'group': '3530901/80202', 'href': '/faculty/95/groups/29909'},
                  {'group': '3530901/80203', 'href': '/faculty/95/groups/30857'},
                  {'group': '3530902/80201', 'href': '/faculty/95/groups/29912'},
                  {'group': '3530902/80202', 'href': '/faculty/95/groups/29913'},
                  {'group': '3530903/80301', 'href': '/faculty/95/groups/29910'},
                  {'group': '3530903/80302', 'href': '/faculty/95/groups/29911'},
                  {'group': '3530904/80101', 'href': '/faculty/95/groups/29895'},
                  {'group': '3530904/80102', 'href': '/faculty/95/groups/29896'},
                  {'group': '3530904/80103', 'href': '/faculty/95/groups/29897'},
                  {'group': '3530904/80104', 'href': '/faculty/95/groups/29898'},
                  {'group': '3530904/80105', 'href': '/faculty/95/groups/29899'},
                  {'group': '3530904/80106', 'href': '/faculty/95/groups/29900'},
                  {'group': '3531201/80201', 'href': '/faculty/95/groups/29901'},
                  {'group': '3532702/80501', 'href': '/faculty/95/groups/29902'},
                  {'group': '3532703/80101', 'href': '/faculty/95/groups/29903'},
                  {'group': '3532704/80201', 'href': '/faculty/95/groups/29906'},
                  {'group': '3532704/80501', 'href': '/faculty/95/groups/29904'},
                  {'group': '3532705/80101', 'href': '/faculty/95/groups/29905'},
                  {'group': '3530202/70201', 'href': '/faculty/95/groups/29921'},
                  {'group': '3530203/70101', 'href': '/faculty/95/groups/29922'},
                  {'group': '3530203/70102', 'href': '/faculty/95/groups/29923'},
                  {'group': '3530901/70101', 'href': '/faculty/95/groups/29936'},
                  {'group': '3530901/70201', 'href': '/faculty/95/groups/29938'},
                  {'group': '3530901/70202', 'href': '/faculty/95/groups/29937'},
                  {'group': '3530901/70203', 'href': '/faculty/95/groups/29939'},
                  {'group': '3530902/70201', 'href': '/faculty/95/groups/29942'},
                  {'group': '3530902/70202', 'href': '/faculty/95/groups/29943'},
                  {'group': '3530903/70301', 'href': '/faculty/95/groups/29940'},
                  {'group': '3530903/70302', 'href': '/faculty/95/groups/29941'},
                  {'group': '3530904/70101', 'href': '/faculty/95/groups/29924'},
                  {'group': '3530904/70102', 'href': '/faculty/95/groups/29925'},
                  {'group': '3530904/70103', 'href': '/faculty/95/groups/29926'},
                  {'group': '3530904/70104', 'href': '/faculty/95/groups/29927'},
                  {'group': '3530904/70105', 'href': '/faculty/95/groups/29928'},
                  {'group': '3530904/70106', 'href': '/faculty/95/groups/29929'},
                  {'group': '3531201/70201', 'href': '/faculty/95/groups/29930'},
                  {'group': '3532702/70501', 'href': '/faculty/95/groups/29931'},
                  {'group': '3532703/70101', 'href': '/faculty/95/groups/29932'},
                  {'group': '3532704/70201', 'href': '/faculty/95/groups/29935'},
                  {'group': '3532704/70501', 'href': '/faculty/95/groups/29933'},
                  {'group': '3532705/70101', 'href': '/faculty/95/groups/29934'}]
        self.assertEqual(parse_group('https://ruz.spbstu.ru/faculty/95/groups/'), groups)
        self.assertEqual(parse_group('https://www.spbstu.ru/'), None)
        
        
    def test_parse_university(self):
        universities = [{'university_name': 'Высшая школа международных образовательных программ', 'university_href': '/faculty/116/groups'},
                        {'university_name': 'Институт физической культуры, спорта и туризма', 'university_href': '/faculty/121/groups'},
                        {'university_name': 'Институт прикладной математики и механики', 'university_href': '/faculty/99/groups'},
                        {'university_name': 'Гуманитарный институт', 'university_href': '/faculty/101/groups'},
                        {'university_name': 'Институт кибербезопасности и защиты информации', 'university_href': '/faculty/122/groups'},
                        {'university_name': 'Институт ядерной энергетики (филиал ФГАОУ ВО СПбПУ) г. Сосновый Бор', 'university_href': '/faculty/120/groups'},
                        {'university_name': 'Институт физики, нанотехнологий и телекоммуникаций', 'university_href': '/faculty/98/groups'},
                        {'university_name': 'Институт промышленного менеджмента, экономики и торговли', 'university_href': '/faculty/100/groups'},
                        {'university_name': 'Институт компьютерных наук и технологий', 'university_href': '/faculty/95/groups'},
                        {'university_name': 'Институт энергетики', 'university_href': '/faculty/93/groups'},
                        {'university_name': 'Институт биомедицинских систем и биотехнологий', 'university_href': '/faculty/119/groups'},
                        {'university_name': 'Институт передовых производственных технологий', 'university_href': '/faculty/111/groups'},
                        {'university_name': 'Институт машиностроения, материалов и транспорта', 'university_href': '/faculty/94/groups'},
                        {'university_name': 'Университетский политехнический колледж', 'university_href': '/faculty/117/groups'},
                        {'university_name': 'Инженерно-строительный институт', 'university_href': '/faculty/92/groups'},
                        {'university_name': 'Высшая  школа биотехнологии и пищевых  технологий', 'university_href': '/faculty/112/groups'},
                        {'university_name': 'Высшая школа техносферной безопасности', 'university_href': '/faculty/96/groups'},
                        {'university_name': 'Институт дополнительного образования', 'university_href': '/faculty/114/groups'}]
        self.assertEqual(parse_university('https://ruz.spbstu.ru'), universities)
        self.assertEqual(parse_university('https://ruz.spbstu.ru/faculty/95/groups/'), None)
    
    
    def test_get_href_on_load(self):
        self.assertRaises(AttributeError, get_href_on_load, 'https://ruz.spbstu.ru')
        self.assertEqual(get_href_on_load('https://ruz.spbstu.ru/faculty/95/groups/29899?date=2020-11-23'), '/faculty/95/groups/29899/ical?date=2020-11-23')
        
        
        today = date.today()
        dayOfWeek = today.weekday()
        if dayOfWeek != 0:
            monday = date.today() - datetime.timedelta(days = dayOfWeek)
        else:
            monday = date.today()
            
        str_day = monday.strftime('%yyyy-%mm-%dd')
        link = '/faculty/95/groups/29899/ical?date=' + str_day
        self.assertEqual(get_href_on_load('https://ruz.spbstu.ru/faculty/95/groups/29899'), link)
     
     
    def test_get_html(self):
        url = 'https://ruz.spbstu.ru/faculty/95/groups/29899'
        bad_url = 'https://ruz.spbstu.ru/faculty/95/groups/404'
        self.assertEqual(get_html(url).status_code, 200)
        self.assertEqual(get_html(bad_url).status_code, 404)

        
if __name__ == '__main__':
    unittest.main()
