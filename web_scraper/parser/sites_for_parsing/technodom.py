from bs4 import BeautifulSoup
from selenium import webdriver
import time
from parser.insert_db import insert_db


def get_products_technodom(page):
    url = 'https://www.technodom.kz/catalog/smartfony-i-gadzhety/smartfony-i-telefony/smartfony?page=' + str(page)
    product = dict()

    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 1700)")
    time.sleep(2)
    main_page = driver.page_source
    html_soup = BeautifulSoup(main_page, 'html.parser')

    name = html_soup.find_all('p', class_='Typography ProductCardV__Title --loading Typography__Body Typography__Body_Bold')
    photo = html_soup.find_all('ul', class_='category-page-list__list')
    photo = photo[0].find_all('picture')
    price = html_soup.find_all('div', class_='ProductCardV__PricesWrapper')
    link = html_soup.find_all('li', class_='category-page-list__item')

    for index, _ in enumerate(photo):
        if photo[index].find('img')['src'].endswith('.jpg'):
            product['photo'] = photo[index].find('img')['src']
            product['name'] = name[index].text
            product['link'] = 'https://www.technodom.kz' + link[index].find('a', class_='category-page-list__item-link')['href']
            product['shop_name'] = 'Technodom'
            if price[index].find('p', class_='Typography ProductCardV__Price ProductCardV__Price_WithOld Typography__Subtitle'):
                product['price'] = price[index].find('p', class_='Typography ProductCardV__Price ProductCardV__Price_WithOld Typography__Subtitle').text
            elif price[index].find('p', class_='Typography ProductCardV__Price Typography__Subtitle'):
                product['price'] = price[index].find('p', class_='Typography ProductCardV__Price Typography__Subtitle').text
            insert_db(product)
        else:
            break


get_products_technodom(1)
