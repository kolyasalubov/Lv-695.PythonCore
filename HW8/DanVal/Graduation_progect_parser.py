import requests
from bs4 import BeautifulSoup
import csv

# URL for parsing
URL = 'https://auto.ria.com/uk/newauto/marka-volvo/'

# For imitation humans
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 '
                         'Safari/537.36', 'accept': 'application/signed-exchange;v=b3;q=0.7,*/*;q=0.8'}
HOST = 'https://auto.ria.com/uk'
FILE = 'cars.csv'


def get_html(url, params=None):
    """function get url page for parsing content
    params - another get requests such as page, brand, city, region"""
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    """To find out the number of pages"""
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())  # number of last page
    else:
        return 1  # category has only one page


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')  # default settings
    items = soup.find_all('section', class_='proposition')  # class_ must have '_'

    my_cars = []
    i = 0
    for item in items:
        my_cars.append({
            # all names of classes hrom HTML tag, from site's page. Tags often changed.
            'title': item.find('h3', class_='proposition_name').find('span', class_='link').get_text(strip=True) + " " + \
                     item.find('div', class_='proposition_equip size13').find('span', class_='link').get_text(
                         strip=True),
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'price_usd': item.find('span', class_='green').get_text(strip=True),
            'city': item.find('span', class_='item region').get('title')
        })      
        i += 1
    return my_cars


def save_file(items, path):
    """Function for saving dana in csv format"""
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Car brand", "Page's link", "USD price", "City"])  # write lines in file
        for item in items:
            writer.writerow([item['title'], item['link'], item['price_usd'], item['city']])


def parse():
    URL = input('Input URL category for parsing\n')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Parsing {page}th of {pages_count} pages...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        save_file(cars, FILE)
    else:
        print('Something went wrong!')


parse()
