"""Парсинг результатов поиска организаций в Яндекс.Картах
   с помощью веб-драйвера и Selenium, и последующее получение
   ссылок на карточки организаций на Яндекс.Картах с помощью
   BeautifulSoup."""


from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup
import time


def get_html_dynamic(url):
    driver = webdriver.Chrome('E:\Coding\Python\Практика\parse_yandex_maps\chromedriver.exe')

    try:
        driver.get(url)
        time.sleep(3)

        while True:
            bottom_element = driver.find_elements_by_class_name('search-snippet-view')

            if driver.find_elements_by_class_name('add-business-view'):
                with open('fullpage.html', 'w', encoding='utf-8') as file:
                    file.write(driver.page_source)
                break
            else:
                move = ActionChains(driver)
                move.move_to_element(bottom_element[-1]).perform()
                time.sleep(0.1)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

def get_info():
    with open('fullpage.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'lxml')
        tags = soup.find_all('a', {'class':'search-snippet-view__link-overlay'})
        for tag in tags:
            url = 'yandex.ru' + tag.get('href')
            with open('urls.txt', 'a', encoding='utf-8') as f:
                f.write(url + '\n')


def main():
    get_html_dynamic('вставить ссылку на поисковый запрос определённых организаций')
    get_info()


if __name__ == '__main__':
    main()


