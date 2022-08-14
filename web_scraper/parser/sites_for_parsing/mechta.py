from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parser.insert_db import insert_db


def get_products_mechta(page):
    url = 'https://www.mechta.kz/section/smartfony/?page=' + str(page)
    product = dict()

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    main_page = driver.page_source
    html_soup = BeautifulSoup(main_page, 'html.parser')

    name = html_soup.find_all('div', class_='q-pt-md q-mt-xs q-px-md text-ts3 text-color2 ellipsis')
    price = html_soup.find_all('div', class_='text-ts1 text-bold q-mr-md text-black')
    photo = html_soup.find_all('div', class_='flex flex-center')
    link = html_soup.find_all('div', class_='q-card')

    for index, _ in enumerate(name):
        product['name'] = name[index].text
        product['price'] = price[index].text.strip()
        product['photo'] = photo[index].find('img')['src']
        product['link'] = link[index].find('a')['href']
        product['shop_name'] = 'mechta'
        insert_db(product)
