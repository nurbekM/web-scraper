from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parser.insert_db import insert_db


def get_products_kaspi(page):
    url = 'https://kaspi.kz/shop/c/smartphones/?q=%3Acategory%3ASmartphones&page=' + str(page)
    product = dict()

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    main_page = driver.page_source
    html_soup = BeautifulSoup(main_page, 'html.parser')

    name_and_link = html_soup.find_all('a', class_='item-card__name-link')
    price = html_soup.find_all('span', class_='item-card__prices-price')
    photo = html_soup.find_all('a', class_='item-card__image-wrapper')

    for index, _ in enumerate(name_and_link):
        product['name'] = name_and_link[index].text
        product['price'] = price[index].text
        product['link'] = name_and_link[index]["href"]
        product['shop_name'] = 'kaspi'
        try:
            product['photo'] = photo[index].find('img')['src']
        except KeyError:
            product['photo'] = photo[index].find('img')['data-src']

        insert_db(product)
