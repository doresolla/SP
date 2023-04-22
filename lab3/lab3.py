from bs4 import BeautifulSoup
import requests

site = 'http://biik.ru/rasp/cg109.htm'  # website
resp = requests.get(site)  # ответ на запрос
resp.encoding = 'windows-1251'  # кодировка сайта
print(resp)  # код ответа
if resp == 404:
    print('Not Found')
else:
    resp = resp.text
    with open("raspisanie.html", "w", encoding='windows-1251') as file:
        file.write(resp)
        file.close()
    bs = BeautifulSoup(resp, "html.parser")  # используется html.parser
    Lesson = bs.findAll('td')  # найти все ячейки таблицы

    with open("Rasp.txt", "w") as file:  # write in file
        for item in Lesson:  # write all text from html tag in txt file
            file.write(item.text + "\n")

    lines = open("Rasp.txt").readlines()  # list all line in txt file
    for i in range(104):  # Удалить первые 102 строки, поскольку они относятся к оформлению сайта
        lines.pop(0)

    with open("Rasp.txt", "w") as f:  # after delete unused elements, write new line in txt file
        for i in range(len(lines) - 1):
            f.write(lines[i])
