import csv
import requests
from bs4 import BeautifulSoup

url = "http://www.fukuokabank.co.jp/atmsearch/?area=%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82%EF%BC%88%E8%A5%BF%E9%83%A8%EF%BC%89"

response = requests.get(url)

response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.content, 'html.parser')

table = bs.findAll("div", {"class":"table_style02_block"})[0]

rows = table.findAll("tr")

csv_list = []

with open("shops.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
