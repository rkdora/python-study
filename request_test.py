# coding: UTF-8
# request_test.py

import requests
from bs4 import BeautifulSoup

# 取得したいURL
url = "https://www.nikkei.com/markets/kabu/"

# urlを引数に指定して、HTTPリクエストを送信してHTMLを取得
response = requests.get(url)

# 文字コードを自動でエンコーディング
response.encoding = response.apparent_encoding

# HTML解析
bs = BeautifulSoup(response.text, 'html.parser')
title_tag = bs.find('title')

# 取得したHTMLを表示
print(title_tag.text)
