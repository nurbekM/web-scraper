from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parser.insert_db import insert_db


def get_products_sulpak(page):
    url = 'https://www.sulpak.kz/f/smartfoniy?page=' + str(page)
    product = dict()


    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    main_page = driver.page_source
    html_soup = BeautifulSoup(main_page, 'html.parser')

    price = html_soup.find_all('div', class_='price')
    product_name = html_soup.find_all('h3', class_='title')
    photo_and_link = html_soup.find_all('div', class_='goods-photo')

    for index, _ in enumerate(photo_and_link):
        product['name'] = product_name[index].text.strip()
        product['price'] = price[index].find_all("span")[1].text
        product['photo'] = photo_and_link[index].find("img")["src"]
        product['link'] = 'https://www.sulpak.kz' + photo_and_link[index].find("a")["href"]
        product['shop_name'] = 'sulpak'
        insert_db(product)
