<p align="center">
    <a href="https://smartproxy.com/"><img src="https://smartproxy.com/wp-content/themes/smartproxy/images/smartproxy-logo.svg" alt="Smartproxy logo" width="200" height="50"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

The following tutorial is meant for educational purposes and introduces to the basics of web scraping and utilizing Smartproxy for it.
We suggest to reseach the [Requests](https://requests.readthedocs.io/en/master/user/quickstart/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) documentation in order to build upon the given example.

### Prerequisites

To run our example scraper, you are going to need these libraries:

* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
* [Requests](https://pypi.org/project/requests/)

## List of contents

- [Introduction](#introduction)
- [Be polite](#be-polite)
- [Let's get to it](#lets-get-to-it)
-- [Inspecting the site](#inspecting-the-site)

## Introduction

If you’re here that means you are interested in finding out more about how to scrape and enjoy all the data that you gather. However, before we dive into it, we first need to understand what web scraping is. In general terms, scraping is the process of acquiring a web page with all of its information and then extracting selected fields for further processing. Usually the purpose of gathering that information is so that a person could easily monitor it. Some examples could be reviews, prices, weather reports, billboard hits,and so on.

## Be polite

Just as you are polite and caring in the real world, you should be such online as well. Before you start scraping, make sure that the website you’re targeting allows it. You can do that by checking its Robots.txt file. If the site doesn’t condone crawling or scraping of its content, be kind and respect the owner’s wishes. Failing to do so might get your IP blocked or even lead to legal action taken against you, so be wary. Moreover, check if the site you’re targeting has an API. If it does, just use that – it will be easier to get the needed data, and you won’t put unnecessary load on the sites infrastructures.

## Let’s get to it

In the following tutorial, you will not only see how a basic scraper is written but will also learn how to adjust it to your own needs. Moreover, you will learn how to do it via a proxy!

As mentioned, we will be using these libraries:
Requests
BeautifulSoup 4
The page we’re going to scrape is http://books.toscrape.com/. It doesn’t have robots.txt, but I think we can agree that the name of the site is asking you to scrape it. But before we carry on with the coding part, let's inspect the website first.

### Inspecting the site

So, this is what the main page of the website looks like. We can see it contains books, their titles, prices, ratings, availability information, and a list of genres in the sidebar.
<p align="center">
    <img src="https://smartproxy.com/wp-content/themes/smartproxy/images/smartproxy-logo.svg" alt="Smartproxy logo" width="200" height="50">
</p>
