<p align="center">
    <a href="https://dashboard.smartproxy.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://i.imgur.com/3uZgYJ9.png"></a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

## Table of contents

- [Disclaimer](#disclaimer)
- [What is web scraping with Python?](#what-is-web-scraping-with-python)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Be polite](#be-polite)
- [How to build a web scraper?](#how-to-build-a-web-scraper)
    - [Inspecting the site](#inspecting-the-site)
    - [Requesting and parsing the data](#requesting-and-parsing-the-data)
    - [Extracting the data](#extracting-the-data)
- [Conclusion](#conclusion)

## Disclaimer

The following tutorial is meant for educational purposes and introduces the basics of building a web scraping project using Smartproxy proxies. You can read more about the [Requests](https://requests.readthedocs.io/en/master/user/quickstart/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) libraries in their documentation to learn more about them and build upon this example.

## What is web scraping with Python?

If you're here, you're probably interested in learning how to scrape valuable data from the web. However, before you dive into it, let's first understand what web scraping is. 

Scraping is an automated process of acquiring a web page with all its content and extracting selected information from it for further processing. The most common purpose of scraping is to avoid the hassle of doing it manually and efficiently, gathering large amounts of data in seconds. Examples include gathering reviews, prices, weather reports, billboard hits, etc.

## Prerequisites

To run the example scraper, you're going to need [Python](https://www.python.org/downloads/) together with these libraries installed:

* [Requests](https://pypi.org/project/requests/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)


## Installation

To install the scraper example, run the following:

```
git clone https://github.com/Smartproxy/Python-scraper-tutorial.git
```

or

```
curl https://raw.githubusercontent.com/Smartproxy/Python-scraper-tutorial/master/scraper.py > scraper.py
```

## Be polite

Just as you are polite and respectful in the real world, you should also be like that online. Before you start scraping, ensure the website you're targeting allows it. You can do that by checking its **Robots.txt** file. If the site doesn't condone crawling or scraping of its content, be kind and respect the rules. Failing to do so might get your IP blocked, rate-limited, or even lead to legal action against you. Moreover, check if the site you're targeting has an API. If it does, use it – getting the needed data will be more straightforward, and you won't put unnecessary load on the website's server.

## How to build a web scraper?

In the following tutorial, you'll learn not only how to write a basic scraper but also how to modify the code according to your own needs. Moreover, you'll also learn how to set it up together with proxies to ensure total anonymity when web scraping.

As mentioned before, you'll be using these libraries:
* [Requests](https://pypi.org/project/requests/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

The page we're going to scrape is http://books.toscrape.com/. It is a website built specifically to test your web scraping scripts. Before going into the example code part, let's inspect the website first.

### Inspecting the site

The following screenshot shows what the main page of the website looks like. You can see it contains books, their titles, prices, ratings, availability information, and a list of genres in the sidebar.

<p align="center">
    <img src="https://i.imgur.com/ovjMkS6.png" alt="books.toscrape.com Main window">
</p>

When you select a specific book, you're taken to a page with even more information, such as its description, how many are in stock, the number of reviews, etc.

<p align="center">
    <img src="https://i.imgur.com/YRy5a1r.png" alt="books.toscrape.com Article window">
</p>

The next step is to decide what information you'd like to extract from this site. Generally, you'll want valuable information you could use later as data. There are many use cases, such as extracting the title and price to compare it to another website, getting direct links to books, checking if they're available, or even getting the descriptions to create an easy-to-read list in a spreadsheet.

Once you know exactly what you want from the site, you can inspect those elements to see how to target them. Look at the site's HTML structure and inspect the elements you need. If you're using Google Chrome, right-click anywhere on the site with your mouse and select **Inspect**. Other web browsers will have an equivalent option to do this, too. 

The Chrome DevTools will open and display the HTML structure of the page. You can manually search for the item you need or use the element picker tool in the top-left corner. Select it, hover over the item you need in the page and it'll find it in the HTML code. After a quick inspection, you can see that the main information on each book is located in the article element with a class name **product_pod**.

![ezgif-5-718c9a2060](https://github.com/Smartproxy/Python-scraper-tutorial/assets/159907476/e229d3f4-1512-42ab-8390-e47a5fdecc5c)


All of the data you'll need is nested in the **article** element. Now, let's inspect the price. We can see that the price value is the text of the paragraph with the **price_color** class. If you inspect the In stock part, you can see that it's a text value of the **instock availability** paragraph. You can check out other elements on the page and see how they're represented in the HTML. Once you're done, let's build a simple web scraper to extract this data through code.

### Requesting and parsing the data

This code aims to write a script that gets the title, price, availability, description, and link to each book and prints it out in a nice, readable format.

Begin writing the script by creating a Python file (.py) in your desired directory. Open the file in a code editor. Your first few lines should import the libraries you'll be using:

```python
import requests
from bs4 import BeautifulSoup
```

You'll need the **Requests** library to send HTTP requests and **BeautifulSoup** to parse the responses you receive from the website. Go ahead and import them.

Then, you'll need to write a GET request to retrieve the contents of the site. Assign the response to the variable ```r```.

The ```requests.get``` function has only one required argument: the URL of the site you're targeting. However, you must pass in an additional proxy parameter because you'll want to use a proxy to reach the content. Declare these variables above your ```requests.get``` statement.

```python
proxy = {'http': 'http://username:password@gate.smartproxy.com:10000'}
url = 'http://books.toscrape.com/'
r = requests.get(url, proxies=proxy)
```

For the proxy, you first need to specify its kind, in this case, HTTP. Then, you have to enter the Smartproxy username and password, separated by a colon, and the endpoint you'll be using to connect to the proxy server. In this example, we're using residential proxies. You can get this information from the dashboard by following these steps:
1. Open the proxy setup tab.
2. Navigate to the Endpoint generator.
3. Configure the parameters according to your needs. Set your authentication method, location, session type, and protocol.
4. Select the number of proxy endpoints you want to generate (you'll only need 1 for now). 
5. Copy the endpoint(s).

<p align="center">
    <a href="https://smartproxy.com/"><img src="https://i.imgur.com/M2J00E4.png"></a>
</p>

The ```url``` parameter is simply the address of the site you want to scrape.

Currently, the variable ```r``` holds the entire response data from the website, including the status code, headers, URL itself, and the content you need. You can add the following line to print the content:
```python
print(r.content)
```

The code so far should look like this:
```python
import requests
from bs4 import BeautifulSoup
proxy = {'http': 'http://username:password@gate.smartproxy.com:10000'}
url = 'http://books.toscrape.com/'
r = requests.get(url, proxies=proxy)
print(r.content)
```
Run the code in your Terminal with:
```
python file_name.py
```

You'll see that it's the site's HTML code you inspected previously. Unfortunately, this data is presented in raw format and is hard to read and understand. The script needs to be improved by parsing only the relevant data you need.

A simple first step in cleaning up our data is to parse HTML with BeautifulSoup. Let's create a variable called ```html```. It will be used to store the parsed ```r.content```. To parse the HTML, you simply need to call the BeautifulSoup class and pass in the content and ```html.parser``` as arguments. Try printing it out!

```python
html = BeautifulSoup(r.content, 'html.parser')
print(html.prettify())
```

It's an optional step, but you can also add ```prettify()```. It's a method that comes with BeautifulSoup, and it makes the HTML even more understandable by adding indentation and presenting the data in a more human-readable format.

### Extracting the data

As you've learned earlier, all the data we need can be found in the **article** elements with the **product_pod** class. To make things easier, you can modify the code to only collect data from these elements specifically. This way, you won't need to parse all of the site's HTML whenever you want to get data about a book. To do so, use one of BeautifulSoup's methods called **find_all()**; it will find all instances of a specified content.

Find and assign all **article** elements with the **product_pod** class to a variable. Let's call it ```all_books```. You need to parse through the ```html``` variable that holds all the HTML with the ```find_all()``` method. As arguments, pass in two attributes: **article**, which is the tag of the content, and the class **product_pod**. Note that because ```class``` is a Python keyword, it can't be used as an argument name, so you need to add a trailing underscore. Here's how it should look like:

```python
all_books = html.find_all('article', class_='product_pod')
```

If you print out ```all_books```, you'll see it contains a list of all the ‘product_pod' articles found on the page.

You've successfully narrowed down the HTML to as much as you need. Now you can start scraping data about the books. Because **all_books** is a list containing all of the necessary information about each book on the page, you'll need to cycle through it using a ```for``` loop:

```python
for book in all_books:
    # Do something
```

```book``` is a variable that you'll call to get specific information in each loop. You can name it however you want, but in our case, ```book``` makes the most sense as you're working with book information in each iteration of the loop of the ```all_books``` list. Remember that we want to find the title, price, availability, description, and link to each book. Let's get started!

When inspecting the site, you can see that the **title** is located as an attribute within the **a** element under **h3**, which is the only one in the **product_pod** scope you're working with.

<p align="center">
    <img src="https://i.imgur.com/odjbJLJ.png" alt="Inspecting the title">
</p>

BeautifulSoup allows you to find a specific element very easily, by just specifying the HTML tags. To find the article, write the following:

```python
title = book.h3.a['title']
```

```book``` is the current iteration of the **product_pod** article, so simply write a path to the information from the parent element ```.h3``` to the ```.a``` to specify which component's data you want to assign to the title. You can also add ```.text``` to get the only the text value of the ```book.h3.a.``` – which is also the title, but longer titles are incomplete and have "..." at the end for styling purposes. Instead, we need to get the value of the title attribute, which can be done by adding ```'title'``` in the square brackets.

If you ```print(title)``` in the loop, you'll see that you've successfully extracted all of the titles of the books on the page. This is what the result should look like:

```
A Light in the Attic
Tipping the Velvet
Soumission
Sharp Objects
Sapiens: A Brief History of Humankind
The Requiem Red
The Dirty Little Secrets of Getting Your Dream Job
The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull       
The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
The Black Maria
Starving Hearts (Triangular Trade Trilogy, #1)
Shakespeare's Sonnets
Set Me Free
Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
Rip it Up and Start Again
Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
Olio
Mesaerion: The Best Science Fiction Stories 1800-1849
Libertarianism for Beginners
It's Only the Himalayas
```

Some objects are not as easy to extract. They may be located in elements nested deep in other elements and containers. In such cases, using the ```find()``` method is easier. It's very similar to the **find_all()** method but only returns the first  element found. You'll want to find the ```p```  with the **price_color** class and extract its text to see the price.

```python
price = book.find('p', class_='price_color').text
```

Next, to find out if the book is in stock, you'll need to do the same thing you did with the price but specify a different paragraph with the **instock availability** class. If you were to print out the availability just like that, you'd see a lot of empty lines because that's how the site's HTML is styled. To fix it, you can use a simple Python method called ```strip()``` to remove any blank spaces or lines from the string. The entire line should look like this:

```python
availability = book.find('p', class_ ='instock availability').text.strip()
```

Lastly, let's get the description of the book. The problem is that it's located on a separate page dedicated to the specific book. To solve this, you'll need to get the link to the said book and make another HTTP request to retrieve the description. If you check the HTML, you'll see that the link is located in the same place as the title. You can create a new variable, copy the command you used for the title, and change the value in the square brackets to ```'href'```.

```python
link_to_book = book.h3.a['href']
```

If you print the ```link_to_book```, you'll see that it contains only a part of the link – the location of where the book can be found on the site, but not the domain. An easy way to solve this is to assign the website's domain link to a variable and add the ```link_to_book``` as a replacement for the placeholder ```{0}``` like this:

```python
link = "http://books.toscrape.com/{0}".format(link_to_book)
```
Now, you have the complete link, which you can use to extract the book's description.
You'll need to make another request inside the ```for``` loop to get it. Simply put, you need to do the same thing as in the beginning: send a GET request to the link and parse the HTML response with BeautifulSoup.

```python
r2 = requests.get(link, proxies=proxy)
html2 = BeautifulSoup(r2.content, 'html.parser')
```

When inspecting the HTML of a book's page, you can see that the description is just plain text stored in a paragraph. However, this paragraph is not the first in the article with a **product_page** class that doesn't have a specified class. If you try to use the ```find()``` method without additional parameters, it will return the price because it's the value in the first paragraph.

<p align="center">
    <img src="https://i.imgur.com/b0SdKSD.png" alt="Inspecting the product description">
</p>

In this case, when using the ```find()``` method, you must state that the paragraph you're looking for has no class (no sass intended). We can do so by specifying that the ```class_``` equals none. Because you just want to get the text value, add ```.text``` at the very end:

```python
description = html2.find('p', class_='').text
```

That's it! You've gathered all the information that you need. You can now print all of it and check the result. Just a quick note: because the description might be long, you can trim it by adding ```[:x]```, where x = number of characters that the description can't exceed.

```python
print(title)
print(price)
print(availability)
print("{0}...".format(description[:150]))
print(link)
print()
```

This is how every book's information will be represented:

```
Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
£52.29
In stock
Scott Pilgrim's life is totally sweet. He's 23 years old, he's in a rockband, he's "between jobs" and he's dating a cute high school girl. Nothing cou...
http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html
```


## Conclusion

That's it! It's important to note that there are a thousand ways to get the data you need by using different functions, loops, etc. The one we've explored here is just one of many, and it can be done in many different approaches. Many challenges can arise when dealing with complex HTML structures.

In this article, you've learned how to write a simple scraper script to get information from a website. While the website is just an example that doesn't employ anti-scraping measures, you've also implemented proxies, ensuring that every request was made anonymously and safely. This knowledge will be beneficial when scraping real websites with actual, valuable data.
 

## Contact
If you need any help or get stuck, feel free to contact us using one of the methods provided:

Email - sales@smartproxy.com

<a href="https://direct.lc.chat/12092754/">Live chat 24/7</a>
