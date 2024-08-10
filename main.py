from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time
import random


browser = webdriver.Firefox()

#Далее одинаково для всех браузеров

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
time.sleep(3)
#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys(input("Введите первоначальный запрос: "))
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(3)

paragraphs = []
hatnotes = []
hatnotes2 = []
tekpar = 0
def read_page(browser):
    global paragraphs
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    print("На этой странице параграфов:", len(paragraphs))
    global tekpar
    tekpar = 0
    global hatnotes
    hatnotes = []
    global hatnotes2
    hatnotes2 = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        #Чтобы искать атрибут класса
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
        if cl == "mw-search-result-heading":
            hatnotes2.append(element)

    print("На этой странице ссылок:", len(hatnotes))
    print("Связанные страницы:", len(hatnotes2))

read_page(browser)

while True:
    rez = input("чтобы листать параграфы нажмите 'п', чтобы выйти нажмите 'в', чтобы перечитать нажмите 'р', чтобы перейти на связанную страницу 'c'")
    if rez == "в":
        break
    elif rez == "р":
        read_page(browser)

    elif rez == "п":
        tekpar += 1
        if tekpar > len(paragraphs):
            tekpar = 1
        print("Параграф:",tekpar," из ",len(paragraphs), "\n",paragraphs[tekpar-1].text)
    elif rez == "с":
        if len(hatnotes2) > 0:
            hatnote2 = random.choice(hatnotes2)
            print("Переход по ссылке: ",hatnote2.text)
            link = hatnote2.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
            read_page(browser)
        else :
            print ("Ссылок не найдено.")
browser.quit()