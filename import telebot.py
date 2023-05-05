import telebot
import datetime
import time
from telebot import types #База
import urllib.request # работа с URLкой
from bs4 import BeautifulSoup #работа с html
bot = telebot.TeleBot('5808317487:AAFSdmLIKJm5o-qCj-_YscwCfaG_mOSOJAU')
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
den = []
links1 = []
links2 = []
links3 = []
k = []
den1 = []
today = datetime.date.today()
day = today.day 
den.append(f'{day}')

today1 = datetime.date.today()
day1 = today1.day + 1
den1.append(f'{day1}')

@bot.message_handler(commands=['start'])#команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('Сегодня')#кнопки
    item2 = types.KeyboardButton('Завтра')
    item3 = types.KeyboardButton('Ближайшие мероприятия')
    markup.add(item1,item2,item3)
    bot.send_sticker(message.chat.id,sticker= "CAACAgIAAxkBAAEHinBj2kQAAabk-zMuD-KmBCpGHvuV__oAAsI_AALgo4IHq7qUe8um6VsuBA")
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name},я умею показывать расписание мероприятий!📜'.format(message.from_user), reply_markup= markup)
    

@bot.message_handler(commands=['help']) #команда
def help(message):
    bot.send_message(message.chat.id,'Хочешь сообщить об ошибке или оставить пожелания? Пиши <a href="https://t.me/van4ka_P">мне</a>', parse_mode='html')
    


@bot.message_handler(commands=['nextweek']) #команда
def help(message):
    bot.send_message(message.chat.id,'В разработке', parse_mode='html')
   
    




@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Завтра':#кнопка
            bot.send_message(message.chat.id,'Загрузка...')
            def site1(url):#1
                response = urllib.request.urlopen(url)
                return response.read()
            def parse1(html):
                soup = BeautifulSoup(html,'lxml')
                link1 = soup.find('div',class_="page-container put-here")
                for link1 in link1.find_all('a'):
                    href = link1.get('href')
                    if href is not None and href != 'https://www.chuvsu.ru/events_category/kultura/' and href != 'https://www.chuvsu.ru/events_category/sotrudnikam/' and href != 'https://www.chuvsu.ru/events_category/studentam/' and href != 'https://www.chuvsu.ru/events_category/abiturientam-shkolnikam/' and  href != 'https://www.chuvsu.ru/events_category/sport/' and href != 'https://www.chuvsu.ru/events_category/dni-otkrytyh-dverej/' and href != 'https://www.chuvsu.ru/events_category/universitetskie-subboty/' and href != 'https://www.chuvsu.ru/events_category/nauka-i-innovaczii/' and href != 'https://www.chuvsu.ru/events_category/universitet/'  :
                        links1.append(href)
                data = soup.find('section',class_='events-three')
                data1 = data.find_all('span')
                for B in data1:
                    b = B.text.strip()
                    s1.append(b)
                soob1 = soup.find('div' ,class_="page-container put-here")
                sobb1 = soob1.find_all('a')
                for A in sobb1:
                    a = A.text.strip()
                    if (a!="Студентам" and a!="Сотрудникам" and a!="Культура" and a != "Наука и инновации" and a != "Спорт / Здоровье" and a != "Абитуриентам / Школьникам" and a != "Университетские субботы" and a != "Дни открытых дверей" and a != "Университет" and a != 'Образование' and a != 'Выпускникам'):
                        s2.append(a)
            def main1():
                parse1(site1('https://www.chuvsu.ru/events/'))
            if __name__ == '__main__':
                main1()
                    
                    
            def site2(url):#2
                response2 = urllib.request.urlopen(url)
                return response2.read()
            def parse2(html):
                soup2 = BeautifulSoup(html,'lxml')
                link2 = soup2.find('div',class_="page-container put-here")
                for link2 in link2.find_all('a'):
                    href = link2.get('href')
                    if href is not None and href != 'https://www.chuvsu.ru/events_category/kultura/' and href != 'https://www.chuvsu.ru/events_category/sotrudnikam/' and href != 'https://www.chuvsu.ru/events_category/studentam/' and href != 'https://www.chuvsu.ru/events_category/abiturientam-shkolnikam/' and  href != 'https://www.chuvsu.ru/events_category/sport/':
                          links2.append(href)
                data2 = soup2.find('section',class_='events-three')
                dataa2 = data2.find_all('span')
                for B2 in dataa2:
                    b2 = B2.text.strip()
                    s3.append(b2)
                soob2 = soup2.find('div', class_="page-container put-here")
                sobb2 = soob2.find_all('a')
                for A2 in sobb2:
                    a2 = A2.text.strip()
                    if (a2!="Студентам" and a2!="Сотрудникам" and a2!="Культура" and a2 != "Наука и инновации" and a2 != "Спорт / Здоровье" and a2 != "Абитуриентам / Школьникам" and a2 != "Университетские субботы" and a2 != "Дни открытых дверей" and a2 != "Университет" and a2 != 'Образование' and a2!=' Спорт / Здоровье' and a2 != 'Выпускникам'):
                        s4.append(a2)
            def main2():
                parse2(site2('https://www.chuvsu.ru/events/page/2/'))
            if __name__ == '__main__':
                main2()
    
            def site3(url):#3
                response3 = urllib.request.urlopen(url)
                return response3.read()
            def parse3(html):
                soup3 = BeautifulSoup(html,'lxml')
                link3 = soup3.find('div',class_="page-container put-here")
                for link3 in link3.find_all('a'):
                    href3 = link3.get('href')
                    if href3 is not None and href3 != 'https://www.chuvsu.ru/events_category/kultura/' and href3 != 'https://www.chuvsu.ru/events_category/sotrudnikam/' and href3 != 'https://www.chuvsu.ru/events_category/studentam/' and href3 != 'https://www.chuvsu.ru/events_category/abiturientam-shkolnikam/' and  href3 != 'https://www.chuvsu.ru/events_category/sport/' and href3 != 'https://www.chuvsu.ru/events_category/dni-otkrytyh-dverej/' and href3 != 'https://www.chuvsu.ru/events_category/universitetskie-subboty/' and href3 != 'https://www.chuvsu.ru/events_category/nauka-i-innovaczii/' and href3 != 'https://www.chuvsu.ru/events_category/universitet/'  :
                        links3.append(href3)
                data3 = soup3.find('section',class_='events-three')
                dataa3 = data3.find_all('span')
                for B2 in dataa3:
                    b3 = B2.text.strip()
                    s5.append(b3)
                soob3 = soup3.find('div', class_="page-container put-here")
                sobb3 = soob3.find_all('a')
                for A3 in sobb3:
                    a3 = A3.text.strip()
                    if (a3!="Студентам" and a3!="Сотрудникам" and a3!="Культура" and a3 != "Наука и инновации" and a3 != "Спорт / Здоровье" and a3 != "Абитуриентам / Школьникам" and a3 != "Университетские субботы" and a3 != "Дни открытых дверей" and a3 != "Университет" and a3 != 'Образование' and a3!=' Спорт / Здоровье'and a3 != 'Выпускникам'):
                        s6.append(a3)
            def main3():
                parse3(site3('https://www.chuvsu.ru/events/page/3/'))
            if __name__ == '__main__':
                main3()
                
            if s5[0] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[0] + ' ' + s5[1] + ' ' +  s5[2] + '  -  ' + s6[0] + ' \n' + links3[0])
            if s5[3] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[3] + ' ' + s5[4] + ' ' +  s5[5] + '  -  ' + s6[1] + ' \n' + links3[1])
            if s5[6] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[6] + ' ' + s5[7] + ' ' +  s5[8] + '  -  ' + s6[2] + ' \n' + links3[2])
            if s5[9] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[9] + ' ' + s5[10] + ' ' +  s5[11] + '  -  ' + s6[3] + ' \n' + links3[3])
            if s5[12] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[12] + ' ' + s5[13] + ' ' +  s5[14] + '  -  ' + s6[4] + ' \n' + links3[4])
            if s5[15] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[15] + ' ' + s5[16] + ' ' +  s5[17] + '  -  ' + s6[5] + ' \n' + links3[5])
            if s5[18] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[18] + ' ' + s5[19] + ' ' +  s5[20] + '  -  ' + s6[6] + ' \n' + links3[6])
            if s5[21] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[21] + ' ' + s5[22] + ' ' +  s5[23] + '  -  ' + s6[7] + ' \n' + links3[7])
            if s5[24]  == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s5[24] + ' ' + s5[25] + ' ' +  s5[26] + '  -  ' + s6[8] + ' \n' + links3[8])
            if s3[0] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[0] + ' ' + s3[1] + ' ' +  s3[2] + '  -  ' + s4[0] + ' \n' + links2[0])
            if s3[3] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[3] + ' ' + s3[4] + ' ' +  s3[5] + '  -  ' + s4[1] + ' \n' + links2[1])
            if s3[6] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[6] + ' ' + s3[7] + ' ' +  s3[8] + '  -  ' + s4[2] + ' \n' + links2[2])
            if s3[9] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[9] + ' ' + s3[10] + ' ' +  s3[11] + '  -  ' + s4[3] + ' \n' + links2[3])
            if s3[12] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[12] + ' ' + s3[13] + ' ' +  s3[14] + '  -  ' + s4[4] + ' \n' + links2[4])
            if s3[15] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[15] + ' ' + s3[16] + ' ' +  s3[17] + '  -  ' + s4[5] + ' \n' + links2[5])
            if s3[18] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[18] + ' ' + s3[19] + ' ' +  s3[20] + '  -  ' + s4[6] + ' \n' + links2[6])
            if s3[21] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[21] + ' ' + s3[22] + ' ' +  s3[23] + '  -  ' + s4[7] + ' \n' + links2[7])
            if s3[24]  == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s3[24] + ' ' + s3[25] + ' ' +  s3[26] + '  -  ' + s4[8] + ' \n' + links2[8])
            if s1[0] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[0] + ' ' + s1[1] + ' ' +  s1[2] + '  -  ' + s2[0] + ' \n' + links1[0])
            if s1[3] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[3] + ' ' + s1[4] + ' ' +  s1[5] + '  -  ' + s2[1] + ' \n' + links1[1])
            if s1[6] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[6] + ' ' + s1[7] + ' ' +  s1[8] + '  -  ' + s2[2] + ' \n' + links1[2])
            if s1[9] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[9] + ' ' + s1[10] + ' ' +  s1[11] + '  -  ' + s2[3] + ' \n' + links1[3])
            if s1[12] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[12] + ' ' + s1[13] + ' ' +  s1[14] + '  -  ' + s2[4] + ' \n' + links1[4])
            if s1[15] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[15] + ' ' + s1[16] + ' ' +  s1[17] + '  -  ' + s2[5] + ' \n' + links1[5])
            if s1[18] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[18] + ' ' + s1[19] + ' ' +  s1[20] + '  -  ' + s2[6] + ' \n' + links1[6])
            if s1[21] == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[21] + ' ' + s1[22] + ' ' +  s1[23] + '  -  ' + s2[7] + ' \n' + links1[7])
            if s1[24]  == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[24] + ' ' + s1[25] + ' ' +  s1[26] + '  -  ' + s2[8] + ' \n' + links1[8])
            if s1[24]  != den1[0] and s1[21] != den1[0] and s1[18] != den1[0] and s1[15] != den1[0] and s1[12] != den1[0] and s1[9] != den1[0] and s1[6] != den1[0] and s1[3] != den1[0] and s1[0] != den1[0] and s3[24]  != den1[0] and s3[21] != den1[0] and s3[18] != den1[0] and s3[15] != den1[0] and s3[12] != den1[0] and s3[9] != den1[0] and s3[6] != den1[0] and s3[3] != den1[0] and s3[0] != den1[0] and s5[24]  != den1[0] and s5[21] != den1[0] and s5[18] != den1[0] and s5[15] != den1[0] and s5[12] != den1[0] and s5[9] != den1[0] and s5[6] != den1[0] and s5[3] != den1[0] and s5[0] != den1[0]:
                bot.send_message(message.chat.id,'Мероприятия не найдены')
        elif message.text == 'Ближайшие мероприятия':#Парсинг Сайта Чгу
            bot.send_message(message.chat.id, "Загрузка...")
            def site1(url):#1
                response = urllib.request.urlopen(url)
                return response.read()
            def parse1(html):
                soup = BeautifulSoup(html,'lxml')
                data = soup.find('section',class_='events-three')
                data1 = data.find_all('span')
                for B in data1:
                    b = B.text.strip()
                    s1.append(b)
                soob1 = soup.find('div' ,class_="page-container put-here")
                sobb1 = soob1.find_all('a')
                for A in sobb1:
                    a = A.text.strip()
                    if a!="Студентам" and a!="Сотрудникам" and a!="Культура" and a != "Наука и инновации" and a != "Абитуриентам / Школьникам" and a != "Университетские субботы" and a != "Дни открытых дверей" and a != "Университет" and a != 'Образование' and a != "Спорт / Здоровье" and a != "Спорт / Здоровье" and a != 'Выпускникам':
                        s2.append(a)
            def main1():
                parse1(site1('https://www.chuvsu.ru/events/'))
            if __name__ == '__main__':
                main1()
                    
                    
            def site2(url):#2
                response2 = urllib.request.urlopen(url)
                return response2.read()
            def parse2(html):
                soup2 = BeautifulSoup(html,'lxml')
                data2 = soup2.find('section',class_='events-three')
                dataa2 = data2.find_all('span')
                for B2 in dataa2:
                    b2 = B2.text.strip()
                    s3.append(b2)
                soob2 = soup2.find('div', class_="page-container put-here")
                sobb2 = soob2.find_all('a')
                for A2 in sobb2:
                    a2 = A2.text.strip()
                    if (a2!="Студентам" and a2!="Сотрудникам" and a2!="Культура" and a2 != "Наука и инновации" and a2 != "Спорт / Здоровье" and a2 != "Абитуриентам / Школьникам" and a2 != "Университетские субботы" and a2 != "Дни открытых дверей" and a2 != "Университет" and a2 != 'Образование'):
                        s4.append(a2)
            def main2():
                parse2(site2('https://www.chuvsu.ru/events/page/2'))
            if __name__ == '__main__':
                main2()
            bot.send_message(message.chat.id
                             , '💥 ' + s2[0] + " - " + s1[0] + " " + s1[1] + " " + s1[2] + '\n' + '💥 ' + s2[1] + " - " + s1[3] + " " + s1[4] + " " + s1[5] + '\n' + '💥 ' + s2[2] + " - " + s1[6] + " " + s1[7] + " " + s1[8] + '\n' + '💥 ' + s2[3] + " - " + s1[9] + " " + s1[10] + " " + s1[11] + '\n' + '💥 ' + s2[4] + " - " + s1[12] + " " + s1[13] + " " + s1[14] + '\n' + '💥 ' + s2[5] + " - " + s1[15] + " " + s1[16] + " " + s1[17] + '\n' + '💥 ' + s2[6] + " - " + s1[18] + " " + s1[19] + " " + s1[20] + '\n' + '💥 ' + s2[7] + " - " + s1[21] + " " + s1[22] + " " + s1[23] + '\n' + '💥 ' + s2[8] + " - " + s1[24] + " " + s1[25] + " " + s1[26] + '\n' + '💥 ' + s4[0]  + " - " + s3[0] + " " + s3[1] + " " + s3[2] + '\n' + '💥 ' + s4[1] + " - " + s3[3] + " " + s3[4] + " " + s3[5] + '\n' + '💥 ' + s4[2] + " - " + s3[6] + " " + s3[7] + " " + s3[8] + '\n' + '💥 ' + s4[3] + " - " + s3[9] + " " + s3[10] + " " + s3[11] + '\n' + '💥 ' + s4[4] + " - " + s3[12] + " " + s3[13] + " " + s3[14] + '\n' + '💥 ' + s4[5] + " - " + s3[15] + " " + s3[16] + " " + s3[17] + '\n' + '💥 ' + s4[6] + " - " + s3[18] + " " + s3[19] + " " + s3[20] + '\n' + '💥 ' + s4[7]+ " - " + s3[21] + " " + s3[22] + " " + s3[23] + '\n' + '💥 ' + s4[8] + " - " + s3[24] + " " + s3[25] + " " + s3[26], 
                             parse_mode='html')
        elif message.text == 'Сегодня':
            bot.send_message(message.chat.id,'Загрузка...')
            def site1(url):#1
                response = urllib.request.urlopen(url)
                return response.read()
            def parse1(html):
                soup = BeautifulSoup(html,'lxml')
                link1 = soup.find('div',class_="page-container put-here")
                for link1 in link1.find_all('a'):
                    href = link1.get('href')
                    if href is not None and href != 'https://www.chuvsu.ru/events_category/kultura/' and href != 'https://www.chuvsu.ru/events_category/sotrudnikam/' and href != 'https://www.chuvsu.ru/events_category/studentam/' and href != 'https://www.chuvsu.ru/events_category/abiturientam-shkolnikam/' and  href != 'https://www.chuvsu.ru/events_category/sport/' and href != 'https://www.chuvsu.ru/events_category/dni-otkrytyh-dverej/' and href != 'https://www.chuvsu.ru/events_category/universitetskie-subboty/' and href != 'https://www.chuvsu.ru/events_category/nauka-i-innovaczii/' and href != 'https://www.chuvsu.ru/events_category/universitet/':
                        links1.append(href)
                data = soup.find('section',class_='events-three')
                data1 = data.find_all('span')
                for B in data1:
                    b = B.text.strip()
                    s1.append(b)
                soob1 = soup.find('div' ,class_="page-container put-here")
                sobb1 = soob1.find_all('a')
                for A in sobb1:
                    a = A.text.strip()
                    if (a!="Студентам" and a!="Сотрудникам" and a!="Культура" and a != "Наука и инновации"  and a != "Абитуриентам / Школьникам" and a != "Университетские субботы" and a != "Дни открытых дверей" and a != "Университет" and a != 'Образование' and a!=' Спорт / Здоровье' and a != 'Выпускникам'):
                        s2.append(a)
            def main1():
                parse1(site1('https://www.chuvsu.ru/events/page/3'))
            if __name__ == '__main__':
                main1()
                    
                    
            def site2(url):#2
                response2 = urllib.request.urlopen(url)
                return response2.read()
            def parse2(html):
                soup2 = BeautifulSoup(html,'lxml')
                link2 = soup2.find('div',class_="page-container put-here")
                for link2 in link2.find_all('a'):
                    href2 = link2.get('href')
                    if href2 is not None and href2 != 'https://www.chuvsu.ru/events_category/kultura/' and href2 != 'https://www.chuvsu.ru/events_category/sotrudnikam/' and href2 != 'https://www.chuvsu.ru/events_category/studentam/' and href2 != 'https://www.chuvsu.ru/events_category/abiturientam-shkolnikam/' and  href2 != 'https://www.chuvsu.ru/events_category/sport/' and href2!= 'https://www.chuvsu.ru/events_category/dni-otkrytyh-dverej/' and href2 != 'https://www.chuvsu.ru/events_category/universitetskie-subboty/' and href2 != 'https://www.chuvsu.ru/events_category/nauka-i-innovaczii/' and href2 != 'https://www.chuvsu.ru/events_category/universitet/'  :
                          links2.append(href2)
                data2 = soup2.find('section',class_='events-three')
                dataa2 = data2.find_all('span')
                for B2 in dataa2:
                    b2 = B2.text.strip()
                    s3.append(b2)
                soob2 = soup2.find('div', class_="page-container put-here")
                sobb2 = soob2.find_all('a')
                for A2 in sobb2:
                    a2 = A2.text.strip()
                    if (a2!="Студентам" and a2!="Сотрудникам" and a2!="Культура" and a2 != "Наука и инновации" and a2 != "Спорт / Здоровье" and a2 != "Абитуриентам / Школьникам" and a2 != "Университетские субботы" and a2 != "Дни открытых дверей" and a2 != "Университет" and a2 != 'Выпускникам' ):
                        s4.append(a2)
            def main2():
                parse2(site2('https://www.chuvsu.ru/events/page/2'))
            if __name__ == '__main__':
                main2()
    
            def site3(url):#3
                response3 = urllib.request.urlopen(url)
                return response3.read()
            def parse3(html):
                soup3 = BeautifulSoup(html,'lxml')
                link3 = soup3.find('div',class_="page-container put-here")
                for link3 in link3.find_all('a'):
                    href3 = link3.get('href')
                    if href3 is not None and href3 != 'https://www.chuvsu.ru/events_category/kultura/' and href3 != 'https://www.chuvsu.ru/events_category/sotrudnikam/' and href3 != 'https://www.chuvsu.ru/events_category/studentam/' and href3 != 'https://www.chuvsu.ru/events_category/abiturientam-shkolnikam/' and  href3 != 'https://www.chuvsu.ru/events_category/sport/' and href3 != 'https://www.chuvsu.ru/events_category/dni-otkrytyh-dverej/' and href3 != 'https://www.chuvsu.ru/events_category/universitetskie-subboty/' and href3 != 'https://www.chuvsu.ru/events_category/nauka-i-innovaczii/' and href3 != 'https://www.chuvsu.ru/events_category/universitet/'  :
                        links3.append(href3)
                data3 = soup3.find('section',class_='events-three')
                dataa3 = data3.find_all('span')
                for B2 in dataa3:
                    b3 = B2.text.strip()
                    s5.append(b3)
                soob3 = soup3.find('div', class_="page-container put-here")
                sobb3 = soob3.find_all('a')
                for A3 in sobb3:
                    a3 = A3.text.strip()
                    if (a3!="Студентам" and a3!="Сотрудникам" and a3!="Культура" and a3 != "Наука и инновации" and a3 != "Спорт / Здоровье" and a3 != "Абитуриентам / Школьникам" and a3 != "Университетские субботы" and a3 != "Дни открытых дверей" and a3 != "Университет" and a3 != 'Образование' and a3 != 'Выпускникам'):
                        s6.append(a3)
            def main3():
                parse3(site3('https://www.chuvsu.ru/events/'))
            if __name__ == '__main__':
                main3()
            if s5[0] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[0] + ' ' + s5[1] + ' ' +  s5[2] + '  -  ' + s6[0] + ' \n' + links3[0])
            if s5[3] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[3] + ' ' + s5[4] + ' ' +  s5[5] + '  -  ' + s6[1] + ' \n' + links3[1])
            if s5[6] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[6] + ' ' + s5[7] + ' ' +  s5[8] + '  -  ' + s6[2] + ' \n' + links3[2])
            if s5[9] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[9] + ' ' + s5[10] + ' ' +  s5[11] + '  -  ' + s6[3] + ' \n' + links3[3])
            if s5[12] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[12] + ' ' + s5[13] + ' ' +  s5[14] + '  -  ' + s6[4] + ' \n' + links3[4])
            if s5[15] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[15] + ' ' + s5[16] + ' ' +  s5[17] + '  -  ' + s6[5] + ' \n' + links3[5])
            if s5[18] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[18] + ' ' + s5[19] + ' ' +  s5[20] + '  -  ' + s6[6] + ' \n' + links3[6])
            if s5[21] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[21] + ' ' + s5[22] + ' ' +  s5[23] + '  -  ' + s6[7] + ' \n' + links3[7])
            if s5[24]  == den[0]:
                bot.send_message(message.chat.id,'🤯' + s5[24] + ' ' + s5[25] + ' ' +  s5[26] + '  -  ' + s6[8] + ' \n' + links3[8])
            if s3[0] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[0] + ' ' + s3[1] + ' ' +  s3[2] + '  -  ' + s4[0] + ' \n' + links2[0])
            if s3[3] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[3] + ' ' + s3[4] + ' ' +  s3[5] + '  -  ' + s4[1] + ' \n' + links2[1])
            if s3[6] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[6] + ' ' + s3[7] + ' ' +  s3[8] + '  -  ' + s4[2] + ' \n' + links2[2])
            if s3[9] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[9] + ' ' + s3[10] + ' ' +  s3[11] + '  -  ' + s4[3] + ' \n' + links2[3])
            if s3[12] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[12] + ' ' + s3[13] + ' ' +  s3[14] + '  -  ' + s4[4] + ' \n' + links2[4])
            if s3[15] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[15] + ' ' + s3[16] + ' ' +  s3[17] + '  -  ' + s4[5] + ' \n' + links2[5])
            if s3[18] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[18] + ' ' + s3[19] + ' ' +  s3[20] + '  -  ' + s4[6] + ' \n' + links2[6])
            if s3[21] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[21] + ' ' + s3[22] + ' ' +  s3[23] + '  -  ' + s4[7] + ' \n' + links2[7])
            if s3[24]  == den[0]:
                bot.send_message(message.chat.id,'🤯' + s3[24] + ' ' + s3[25] + ' ' +  s3[26] + '  -  ' + s4[8] + ' \n' + links2[8])
            if s1[0] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[0] + ' ' + s1[1] + ' ' +  s1[2] + '  -  ' + s2[0] + ' \n' + links1[0])
            if s1[3] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[3] + ' ' + s1[4] + ' ' +  s1[5] + '  -  ' + s2[1] + ' \n' + links1[1])
            if s1[6] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[6] + ' ' + s1[7] + ' ' +  s1[8] + '  -  ' + s2[2] + ' \n' + links1[2])
            if s1[9] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[9] + ' ' + s1[10] + ' ' +  s1[11] + '  -  ' + s2[3] + ' \n' + links1[3])
            if s1[12] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[12] + ' ' + s1[13] + ' ' +  s1[14] + '  -  ' + s2[4] + ' \n' + links1[4])
            if s1[15] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[15] + ' ' + s1[16] + ' ' +  s1[17] + '  -  ' + s2[5] + ' \n' + links1[5])
            if s1[18] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[18] + ' ' + s1[19] + ' ' +  s1[20] + '  -  ' + s2[6] + ' \n' + links1[6])
            if s1[21] == den[0]:
                bot.send_message(message.chat.id,'🤯' + s1[21] + ' ' + s1[22] + ' ' +  s1[23] + '  -  ' + s2[7] + ' \n' + links1[7])
            if s1[24]  == den1[0]:
                bot.send_message(message.chat.id,'🤯' + s1[24] + ' ' + s1[25] + ' ' +  s1[26] + '  -  ' + s2[8] + ' \n' + links1[8])
            if s1[24]  != den[0] and s1[21] != den[0] and s1[18] != den[0] and s1[15] != den[0] and s1[12] != den[0] and s1[9] != den[0] and s1[6] != den[0] and s1[3] != den[0] and s1[0] != den[0] and s3[24]  != den[0] and s3[21] != den[0] and s3[18] != den[0] and s3[15] != den[0] and s3[12] != den[0] and s3[9] != den[0] and s3[6] != den[0] and s3[3] != den[0] and s3[0] != den[0] and s5[24]  != den[0] and s5[21] != den[0] and s5[18] != den[0] and s5[15] != den[0] and s5[12] != den[0] and s5[9] != den[0] and s5[6] != den[0] and s5[3] != den[0] and s5[0] != den[0]:
                bot.send_message(message.chat.id,'Мероприятия не найдены')
                
        else:
             bot.send_message(message.chat.id, 'Нормально пиши')
             
bot.polling(none_stop= True)