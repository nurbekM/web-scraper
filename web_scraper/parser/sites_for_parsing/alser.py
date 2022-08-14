from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parser.insert_db import insert_db


def get_products_alser(page):
    url = 'https://alser.kz/c/vse-smartfony/page-' + str(page)
    product = dict()

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    main_page = driver.page_source
    html_soup = BeautifulSoup(main_page, 'html.parser')

    name = html_soup.find_all('a', class_='product-item__info_title')
    price = html_soup.find_all('div', class_='price')
    photo_and_link = html_soup.find_all('div', class_='product-item__front')

    for index, _ in enumerate(name):
        product['name'] = name[index].text.replace('\n', '')
        product['price'] = price[index].text.strip()
        product['photo'] = photo_and_link[index].find('img')['src']
        product['link'] = 'https://alser.kz' + photo_and_link[index].find('a', class_='product-item__image')['href']
        product['shop_name'] = 'alser'

        insert_db(product)
