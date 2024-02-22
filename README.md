<p align="center">
    <a href="https://dashboard.smartproxy.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://i.imgur.com/3uZgYJ9.png"></a>
</p>

### Disclaimer

The following tutorial is meant for educational purposes and introduces to the basics of web scraping and utilizing Smartproxy for it.
We suggest to reseach the [Requests](https://requests.readthedocs.io/en/master/user/quickstart/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) documentation in order to build upon the given example.

### Prerequisites

To run our example scraper, you are going to need these libraries:

* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
* [Requests](https://pypi.org/project/requests/)

### Installation

To install the scraper example run:

`git clone https://github.com/Smartproxy/Python-scraper-tutorial.git`

or

`curl https://raw.githubusercontent.com/Smartproxy/Python-scraper-tutorial/master/scraper.py > scraper.py`

## List of contents

- [Introduction](#introduction)
- [Be polite](#be-polite)
- [Let's get to it](#lets-get-to-it)
    - [Inspecting the site](#inspecting-the-site)
    - [Requesting and parsing the data](#requesting-and-parsing-the-data)
    - [Extracting the data](#extracting-the-data)
- [Conclusion](#conclusion)

## Introduction

If you’re here that means you are interested in finding out more about how to scrape and enjoy all the data that you gather. However, before we dive into it, we first need to understand what web scraping is. In general terms, scraping is the process of acquiring a web page with all of its information and then extracting selected fields for further processing. Usually the purpose of gathering that information is so that a person could easily monitor it. Some examples could be reviews, prices, weather reports, billboard hits,and so on.

## Be polite

Just as you are polite and caring in the real world, you should be such online as well. Before you start scraping, make sure that the website you’re targeting allows it. You can do that by checking its **Robots.txt** file. If the site doesn’t condone crawling or scraping of its content, be kind and respect the owner’s wishes. Failing to do so might get your IP blocked or even lead to legal action taken against you, so be wary. Moreover, check if the site you’re targeting has an API. If it does, just use that – it will be easier to get the needed data, and you won’t put unnecessary load on the sites infrastructures.

## Let’s get to it

In the following tutorial, you will not only see how a basic scraper is written but will also learn how to adjust it to your own needs. Moreover, you will learn how to do it via a proxy!

As mentioned, we will be using these libraries:
Requests
BeautifulSoup 4
The page we’re going to scrape is http://books.toscrape.com/. It doesn’t have robots.txt, but I think we can agree that the name of the site is asking you to scrape it. But before we carry on with the coding part, let's inspect the website first.
First off, let’s import the libraries we’ll be using:

### Inspecting the site

So, this is what the main page of the website looks like. We can see it contains books, their titles, prices, ratings, availability information, and a list of genres in the sidebar.

<p align="center">
    <img src="https://i.imgur.com/ovjMkS6.png" alt="books.toscrape.com Main window" width="600" height="500">
</p>

When we select a specific book, we are greeted with even more information, such as its description, how many are in stock, the number of reviews, etc.

<p align="center">
    <img src="https://i.imgur.com/YRy5a1r.png" alt="books.toscrape.com Article window" width="600" height="500">
</p>

Great! Now we can think about what information we’d like to extract from this site. Generally, when scraping, we want to get valuable information which we could use later on. In this example, the most important points would be the price and the title of the book, so we could, for example, make a comparison with books on another website. We can also extract the direct link to a book, so it would be easier to reach later on. Finally, it would be great to know if the book is even available. As a finishing touch, we can scrape its description as well – perhaps it might catch your eye and you’ll read it.

So, now that we know exactly what we want to get from the site, we can go on and inspect those elements to see where they can be found later. Just a note: you don’t need to memorise everything now; when scraping, you’ll have to go back to the HTML code numerous times. Let’s have a look at the site’s code and inspect the elements we need. To do so, just right-click anywhere on the site with your mouse and select “Inspect”.

Once you do that, a gazillion things will open – but don’t worry, we don't need to go through all of them. After a quick inspection, we can see that all the data we need is located in the article element with a class name **product_pod**. The same is for all other books, as well.

<p align="center">
    <img src="https://i.imgur.com/QbdDzyW.png" alt="books.toscrape.com Inspecting the HTML" width="1000" height="500">
</p>

This means that all the data we need will be nested in that article element. Now, let’s inspect the price. We can see that the price value is the text of the **price_color** paragraph. And if we inspect In stock, we can see that it is a text value of the **instock availability** paragraph. Now go on and get familiar with the rest of the elements we’ll be scraping. Once you're done, we need to get coding and turn our data extraction wishes into reality.

### Requesting and parsing the data

First off, let’s import the libraries we’ll be using:
<p align="center">
    <img src="https://i.imgur.com/eIpTBBJ.png" alt="books.toscrape.com Libraries" width="600" height="50">
</p>

We’ll need the **Requests** library to send HTTP requests and **BeautifulSoup** to parse the responses we receive from the website. Go ahead and import them.
Then, we’ll need to write a GET request to retrieve the contents of the site. Lets assign the response to the variable **r**.

<p align="center">
    <img src="https://i.imgur.com/7kAQtEY.png" alt="Writing the request" width="600" height="50">
</p>

The **requests.get** function has only one required argument, which is the URL of the site you are targeting. However, because we wish to use a proxy to reach the content, we need to pass in an additional proxies parameter. As you can see, both values are already assigned to variables, so let’s have a look at them.

<p align="center">
    <img src="https://i.imgur.com/KiS9NSP.png" alt="Request's variables" width="600" height="50">
</p>

For the proxy, we first need to specify its kind, in this case, HTTP. Then, we have to enter the Smartproxy user’s username and password, separated by a colon, as well as the endpoint which we’ll be using to connect to the proxy server. And, well, the **url** is the address of the site we wish to scrape.

At the moment, the variable **r** holds the full  response data from the website, including the status code, headers, URL itself, and, most importantly, the content we need. You can print it out with **print(r.content)**, and you’ll see that it’s the HTML code of the site you inspected previously. However, this time it’s on your device! (Except that it’s awkwardly formatted and unreadable, but we’ll fix that.) https://i.imgur.com/fzV4P8D.png

To start working with the HTML code, we first need to parse it with BeautifulSoup – make a parse tree which we can use to extract the necessary information. Let’s create a variable called **html**. We’ll use it to store the parsed **r.content**. To parse the HTML code, we just need to call the BeautifulSoup class and pass in the content and ‘html.parser’ (‘cause, you know, we are parsing HTML content here) as arguments. Try printing it out!

<p align="center">
    <img src="https://i.imgur.com/fzV4P8D.png" alt="Parsing the HTML" width="600" height="50">
</p>

If you noticed in the image above, I used prettify(). It’s a method that comes with BeautifulSoup, and it makes the HTML even more understandable by adding indents and things like that.

### Extracting the data

As we found out earlier, all the data we need can be found in the **product_pod** articles. So, to make our lives easier, we can collect and work only with them. This way, we won’t need to parse all of the site’s HTML each time we want to get any data about a book. To do so, we can use one of BeautifulSoup’s methods called **find_all()**; it will find all instances of specified content.

So, in our case, we need to find and assign all **articles** with the **product_pod** class to a variable. Let’s call it **all_books**. Now we need to parse through the html variable which we created earlier and which holds the entire HTML of the site. We’ll use the **find_all()** method to do so. As arguments for the **find_all()** method, we need to pass in two attributes: ‘article’, which is the tag of the content, and the class **product_pod**. Please note that because class is a Python keyword, it can’t be used as an argument name, so you need to add a trailing underscore. Here’s how it should look like:

<p align="center">
    <img src="https://i.imgur.com/io8Kr21.png" alt="Assigning book data to a variable" width="600" height="50">
</p>

Now, if you print out **all_books**, you’ll see that it contains a list of all the ‘product_pod’ articles found in the page.

We’ve narrowed down the HTML to as much as we need. Now we can start gathering data about the books. Because **all_books** is a list containing all the necessary information about each book in the page, we’ll need to cycle through it using a **for** loop. Like this:

##### for book in all_books:

**book** is just a variable we created which we’ll be calling to get specific information in each loop. You can name it however you wish, but in our case, **book** is exactly what we are working with each iteration of the loop in the **all_books** list. Remember that we want to find the title, price, availability, description, and the link to each book. Let’s get started!

When inspecting the site, we can see that the title is located in the h3 element, which is the only one in the **product_pod** article we’re working with.

<p align="center">
    <img src="https://i.imgur.com/odjbJLJ.png" alt="Inspecting the title" width="600" height="500">
</p>

BeautifulSoup allows you to find a specific element very easily, by just specifying the HTML tags. To find the article, all we need to write is this:

<p align="center">
    <img src="https://i.imgur.com/OeRHGkb.png" alt="Assigning the title" width="600" height="50">
</p>

Once again, **book** is just the current iteration of the **product_pod** article, so we can just add **.h3** and **.a** to specify which component’s data we want to assign to the title. We could also add **.text** to get the text value of the **book.h3.a.** – which is indeed the title, but if you noticed, longer titles are not complete and have “...” at the end for styling purposes. That’s not really what we need. Instead, we need to get the value of the title element, which can be done by just adding **‘title’** in the square brackets.

If we run **print(title)**, you’ll see that we have successfully extracted all the titles of the books in the page.

<p align="center">
    <img src="https://i.imgur.com/TpCaTPJ.png" alt="Title variable output" width="600" height="500">
</p>

Some objects are not as easy to extract. They may be located in paragraphs, nested in other paragraphs further nested in other div containers. In such cases, it’s easier to use the **find()** method. It’s very similar to the **find_all()** method, however, it only returns the first found element – in our case, that’s exactly what we need. To find the price, we want to find the paragraph with the **price_color** class and extract its text.

<p align="center">
    <img src="https://i.imgur.com/QSQ9RyR.png" alt="Assigning the price" width="600" height="50">
</p>

To find out if the element is in stock, we need to do the same thing we did with the price, simply specify a different paragraph. That would be the one containing the **instock availability** class. If you were to print out the availability just like that, you’d see a lot of blank lines. It’s just the way the site’s  HTML is styled. To combat that, we can use a simple Python method called **strip()**, which will remove any blank spaces or lines from the string. If you’ve done everything correctly, it should look like this:

<p align="center">
    <img src="https://i.imgur.com/8cKQuyN.png" alt="Assigning the availability" width="600" height="50">
</p>

Furthermore, we need to get the description of the book. The problem is that it’s located on another page dedicated to the specific book. First, we need to get the link to the said book and make another HTTP request to retrieve the description. While inspecting, you’ll see that the link occupies the same place as the title. You can create a new variable, copy the command you used for the title, and just change the value in the square brackets to ‘href’, as that’s what we’re looking for there.

<p align="center">
    <img src="https://i.imgur.com/iD0YDZO.png" alt="Assigning the link to a book" width="600" height="50">
</p>

But, if you print out **link_to_book**, you’ll see that it contains only a part of the link - the location of where the book can be found on the site, but not the domain. One easy way to solve this is to assign the website’s domain link to a variable and just add the **link_to_book**, like this:

<p align="center">
    <img src="https://i.imgur.com/5XqNMqC.png" alt="Link variable" width="600" height="50">
</p>
Boom! Now you have the complete link, which we can use to extract the book’s description.

To get the description, we need to make another request inside the **for** loop, so we get one for each of the books. Basically, we need to do the same thing we did in the beginning: send a GET request to the link and parse the HTML response with BeautifulSoup.

<p align="center">
    <img src="https://i.imgur.com/TmXYIKR.png" alt="Second request" width="600" height="50">
</p>

When inspecting the HTML of a book’s page, we can see that the description is just plain text stored in a paragraph. However, this paragraph is not the first in the **product_page** article and does not have a specified class. If we just try to use **find()** without any additional parameters, it will return the price because it’s the value located in the very first paragraph.

<p align="center">
    <img src="https://i.imgur.com/b0SdKSD.png" alt="Inspecting the product description" width="600" height="500">
</p>

In such a case, when using the **find()** method, we need to state that the paragraph we’re looking for has no class (no sass intended). We can do so by specifying that the **class_** equals none.

<p align="center">
    <img src="https://i.imgur.com/WWFltGp.png" alt="Assigning the description" width="600" height="50">
</p>
And, of course, because we just want to get the text value, we add **.text** at the very end

That’s it! We’ve gathered all the information that we needed. We can now print it all out and check what we’ve got. Just a quick note: because the description might be quite long, you can trim it by adding **[:x]**, where x = number of characters you want to print. Some Python tricks for you!

<p align="center">
    <img src="https://i.imgur.com/rwnjf5X.png" alt="Printing the variables" width="600" height="200">
</p>

And the response we get, which is just beautiful:

<p align="center">
    <img src="https://i.imgur.com/tsKfXni.png" alt="All variable output" width="800" height="650">
</p>

## Conclusion

To conclude, I would just like to note that there really are a thousand ways to get the data you need by using different functions, loops, and so on. But we sure hope that by the end of this article, you have a better idea of what, when, and how to scrape, and do it with **proxies**!
