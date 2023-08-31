import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    url = selector.css(".entry-title a::attr(href)").getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    """Pegamos o link da próxima página pela classe next, caso exista"""
    next_url = selector.css(".nav-links a.next::attr(href)").get()
    return next_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".url.fn.n::text").get()
    reading_time_str = selector.css(".meta-reading-time::text").get()
    """Método re.findall para pegar apenas os números da string:
    https://pythonexamples.org/
    python-regex-extract-find-all-the-numbers-in-string/"""
    reading_time = int(re.findall("[0-9]+", reading_time_str)[0])
    summary = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()
    category = selector.css(".category-style .label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": "".join(summary).strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
