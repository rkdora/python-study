# coding: UTF-8
# request_test.py

import requests
from bs4 import BeautifulSoup

# 取得したいURL
url = "http://www.fukuokabank.co.jp/atmsearch/?area=%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82%EF%BC%88%E8%A5%BF%E9%83%A8%EF%BC%89"

# urlを引数に指定して、HTTPリクエストを送信してHTMLを取得
response = requests.get(url)

# 文字コードを自動でエンコーディング
response.encoding = response.apparent_encoding

# HTML解析
bs = BeautifulSoup(response.text, 'html.parser')
title_tag = bs.find('title')

# 取得したHTMLを表示
print(title_tag.text)
