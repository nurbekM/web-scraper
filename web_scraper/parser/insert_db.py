import sqlite3


def insert_db(data):
    try:
        connection = sqlite3.connect('/home/nurbek/Desktop/WebScraper/web_scraper/db.sqlite3')
        cursor = connection.cursor()
        print('Connected')
        result = [elem for elem in data['price'] if elem.isdigit()]
        data['price'] = int(''.join(result))

        sql_request =  "INSERT INTO Phones('name', price, photo, link, shop_name) " \
                      f"VALUES ('{data['name']}', {data['price']}, '{data['photo']}', '{data['link']}', '{data['shop_name']}');"
        cursor.execute(sql_request)
        connection.commit()

    except sqlite3.Error as error:
        print('Er', error)
    finally:
        connection.close()

        print('Connection closed\n')
