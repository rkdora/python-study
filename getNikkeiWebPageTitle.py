# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/markets/kabu/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

span = soup.find_all("span")

nikkei_heikin = ""

for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in "mkc-stock_prices":
            nikkei_heikin = tag.string

            break

    except:
        pass

print nikkei_heikin
