from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parser.insert_db import insert_db


def get_products_beli_veter(page):
    url = 'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1=' + str(page)
    product = dict()

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    main_page = driver.page_source
    html_soup = BeautifulSoup(main_page, 'html.parser')

    name = html_soup.find_all('h4', class_='bx_catalog_item_title_text')
    price = html_soup.find_all('span', class_='bx-more-price-text')

    for index, _ in enumerate(name):
        print(name[index].text)
        print(price[index].text)
        print()


get_products_beli_veter(1)