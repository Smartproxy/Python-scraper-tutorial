import requests
from bs4 import BeautifulSoup

proxy = {'http': 'http://username:password@gate.smartproxy.com:10000'} # Proxy authentication information
url = 'http://books.toscrape.com/' # Website to make a GET request to

r = requests.get(url, proxies=proxy) # Make the GET request to a target URL using proxies
html = BeautifulSoup(r.content, 'html.parser') # Parse the HTML

all_books = html.find_all('article', class_='product_pod') # Find all article elements with the class "product_pod"

for book in all_books: # Loop through each element and find the title, price, availability, and description
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_ ='instock availability').text.strip()
    link_to_book = book.h3.a['href']
    link = "http://books.toscrape.com/{0}".format(link_to_book)

    r2 = requests.get(link, proxies=proxy) # Make a new request to the URL extracted earlier
    html2 = BeautifulSoup(r2.content, 'html.parser')
    description = html2.find('p', class_='').text

    print(title)
    print(price)
    print(availability)
    print("{0}...".format(description[:150])) # Truncate text that is too long (over 150 characters)
    print(link)
    print() # Print an empty line to separate each result
