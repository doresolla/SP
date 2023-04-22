from bs4 import BeautifulSoup
import requests

site = 'http://biik.ru/rasp/cg109.htm'  # website
resp = requests.get(site)  # ответ на запрос
resp.encoding = 'windows-1251'  # кодировка сайта
print(resp)  # код ответа
if resp == 404:
    print('Not Found')
else:
    resp=resp.text
    with open("raspisanie.html", "w", encoding='windows-1251') as file:
        file.write(resp)
        file.close()

