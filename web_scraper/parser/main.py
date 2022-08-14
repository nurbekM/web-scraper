from sites_for_parsing.sulpak import get_products_sulpak
from sites_for_parsing.kaspi import get_products_kaspi
from sites_for_parsing.technodom import get_products_technodom
from sites_for_parsing.mechta import get_products_mechta
from sites_for_parsing.alser import get_products_alser
from selenium.common.exceptions import WebDriverException


function_massive = [
    get_products_sulpak, get_products_kaspi, get_products_technodom, get_products_mechta, get_products_alser
]


def parsing(function):
    for page in range(1, 25):
        try:
            function(page)
        except WebDriverException as ex:
            print('Error... retry parsing...\n')
            function(page)
            continue
        except IndexError as ex:
            print(ex)
            break

#
# for elem in function_massive:
#     parsing(elem)
parsing(get_products_alser)