import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime as dt
import re
from collections import Counter


#菊花賞のデータをとってくる
race_id = "202109040611"
url_base = "https://db.netkeiba.com/race/"

url = url_base + race_id
race_html = requests.get(url)
race_html.encoding = race_html.apparent_encoding
race_soup = BeautifulSoup(race_html.text, 'html.parser')
print(url)

race_soup.find_all("tr",class_="even")
