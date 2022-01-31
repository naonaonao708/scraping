import selenium
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.support.select import Select

def create_odds_id(axis_horse_number):
    odds_id_list = []
    for i in range(1,17,1):
        for j in range(1,17,1):
            if(axis_horse_number==i or axis_horse_number==j):
                continue
            if i==j:
                continue
            odds_id = "odds-8-"+str(axis_horse_number).zfill(2)+str(i).zfill(2)+str(j).zfill(2)
            odds_id_list.append(odds_id)
    return odds_id_list


