from bs4 import BeautifulSoup
import requests
from bs4.element import Comment
import re
import random

# get all url from each /url and eliminate the None and https
def scrape_all(url):
    r = requests.get("https://www.makeschool.com/")
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    word_scrapped = []

    for link in soup.find_all("a"):
        raw = link.get("href")
        if raw is not None:
            if "@" not in raw and "https" not in raw and "http" not in raw:
                word_scrapped.extend(scrape_one("https://www.makeschool.com/" + raw))
    return word_scrapped

# # scrape every /url page
def scrape_one(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    word_scrapped = cleaned_text()
    return word_scrapped

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def cleaned_text():
    r = requests.get("https://www.makeschool.com/")
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    test = soup.find_all(text = True)
    visible = filter(tag_visible, test)
    text =  u"".join(t.strip() for t in visible)
    # get rid of the marks and symbols
    text = re.sub(r'[^A-Za-z]', ' ', text)
    # get rid of double space
    text = re.sub(' +', ' ', text)
    text = text.split(" ")
    word = [s for s in text if len(s) >4]
    return word

def load_word():
    secret = random.choice(cleaned_text())
    return secret.lower()


print(load_word())
