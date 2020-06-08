import requests
from bs4 import BeautifulSoup

proxy = {'http': 'http://SPusername:SPpassword@gate.smartproxy.com:7000'}
url = 'http://books.toscrape.com/catalogue/page-1.html'

r = requests.get(url, proxies=proxy)
html = BeautifulSoup(r.content, 'html.parser')

all_books = html.find_all('article', class_='product_pod')

for book in all_books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_ ='instock availability').text.strip()
    link_to_book = book.h3.a['href']

    link = "http://books.toscrape.com/catalogue/{0}".format(link_to_book)

    r2 = requests.get(link)
    html2 = BeautifulSoup(r2.content, 'html.parser')

    description = html2.find('p', class_='').text

    print(title)
    print(price)
    print(availability)
    print("{0}...".format(description[:150]))
    print(link)
    print()