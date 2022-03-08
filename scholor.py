from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = requests.get("https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&num=10&q=SnRK2")
soup = BeautifulSoup(url.content, "html.parser")


soup.find_all("div")

