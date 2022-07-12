"""Получение ссылок на товары с сайта Wildberries с помощью простых запросов
   и вывод их в текстовый файл."""

import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
product_pattern = 'https://www.wildberries.ru/catalog/{}/detail.aspx?targetUrl=XS'


def get_url(url):
    response = requests.get(url=url, headers=headers).json()
    if not response['data']['products']:
        return False

    with open('urls.txt', 'a', encoding='utf-8') as file:
        for product in response['data']['products']:
            file.write(product_pattern.format(product['id']) + '\n')
    
    return True


def get_all_products(url):
    flag = True
    page_number = 1 

    while flag:
        flag = get_url(url.format(page_number))
        page_number += 1
        

def main():
    url = 'ссылка на поисковый запрос Wildberries'
    get_all_products(url)


if __name__ == '__main__':
    main()
