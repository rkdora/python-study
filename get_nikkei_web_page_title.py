# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

while True:

    if datetime.now().minute != 59:
        time.sleep(58)
        continue

    f = open('nikkei_heikin.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')

    while datetime.now().second != 59:
        time.sleep(1)

    time.sleep(1)

    csv_list = []

    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    csv_list.append(time_)

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


    print time_, nikkei_heikin

    csv_list.append(nikkei_heikin)
    writer.writerow(csv_list)
    f.close()
