import csv
import requests
import bs4
import pandas as pd

#菊花賞のデータをとってくる
race_id = "202109040611"
url_base = "https://db.netkeiba.com/race/"

url = url_base + race_id
