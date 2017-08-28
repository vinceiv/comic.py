import urllib2
import os
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver

debug = False
url = 'http://readcomicbooksonline.net/reader/'
download_folder = "downloads"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"}
driver = webdriver.Firefox()

def initScraper(web_url):
    req = urllib2.Request(web_url, None, headers)
    page = urllib2.urlopen(req).read()
    soup = BeautifulSoup(page, "lxml")
    scrape(soup)

def scrape(arg):
    global driver

    div = arg.find("div", {"id": "omv"})
    for p in div.find_all("img", class_='picture'):
        image_url = url + str(p.get('src'))
        
        parse = str(p.get('src'))
        parsed = parse.split('/')
        issue = parsed[2] 
        comicpage = parsed[3]

        driver.get(image_url)
        images = driver.find_elements_by_tag_name('img')
        
        #if image cant be pulled throw error
        for image in images:
            request = urllib2.Request(image.get_attribute('src'), None, headers)
            data = urllib2.urlopen(request)

            savelocation = os.path.join(download_folder + "/" + parsed[2])
            if not os.path.exists(savelocation):
                os.makedirs(savelocation)
            with open( os.path.join(savelocation, comicpage) ,'wb') as f:
                f.write(data.read())
    nextPage(div)

def nextPage(arg1):
    if arg1.find(title="Next Page"):
        nextPageElem = arg1.find(title="Next Page")
        nextPageAtag = nextPageElem.find_parent("a")
        _url = nextPageAtag.get('href')
        initScraper(url + str(_url))

if __name__ == "__main__":
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    initScraper(url + str(sys.argv[1]))