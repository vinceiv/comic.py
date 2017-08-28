# Comicpy
This program is a proof of concept web scraper that scrapes comic book scan sites for offline viewing.

## Supported sites
[readcomicbooksonline](http://readcomicbooksonline.net)

## Dependencies
- [Selenium](http://selenium-python.readthedocs.io/installation.html#)
```
pip install selenium
```
- [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
```
pip install beautifulsoup4
```

## How to use
Take the second part of the url to the webcomic ex: http://readcomicbooksonline.net/reader/**Batman_Beyond_2016/Batman_Beyond_Issue_11**
```
python scraper.py Batman_Beyond_2016/Batman_Beyond_Issue_11
```

## To do
- Add support for other sites
- Parse url 
- Man page
- Flags
- Turn off geckodriver log