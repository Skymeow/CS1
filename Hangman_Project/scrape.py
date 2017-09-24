from bs4 import BeautifulSoup
import requests

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
                print(raw)
                word_scrapped.extend(scrape_one(url + raw))
    return word_scrapped

# scrape every /url page
def scrape_one(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    word_scrapped = cleaned_text(soup)
    return word_scrapped

def cleaned_text(s):
    return text
