import selenium
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np


def create_odds_id(axis_horse_number):
   odds_id_list = []
   for i in range(1,17,1):
       for j in range(1,17,1):
           if (axis_horse_number==i or axis_horse_number==j):
               continue
           if i==j:
               continue
           odds_id = "odds-8-" + str(axis_horse_number).zfill(2) + str(i).zfill(2) + str(j).zfill(2)
           odds_id_list.append(odds_id)
   return odds_id_list

#オッズリストの作成
def create_odds_list(odds_id_list):
   odds_list = {}
   for odds_id in odds_id_list:
       try:
           odds = table.find_element_by_id(odds_id).text
           odds_list[odds_id[7:]] = odds
       except:
           break
   return odds_list

def change_axis_horse(axis_horse_number):
   #軸馬の選択・変更 dropdown select状態にする
   #select要素を取得
   dropdown = browser.find_element_by_id('list_select_horse')
   #Selectオブジェクト作成
   select = Select(dropdown)
   # valueがaxis_horse_numberのoptionタグを選択状態にする
   select.select_by_value(str(axis_horse_number))
   
browser = webdriver.Chrome()
browser.get('https://race.netkeiba.com/odds/index.html?type=b8&race_id=202106010411&housiki=c0&rf=shutuba_submenu')

odds_all_list = {}
for axis_horse_number in range(1,17,1):
   if axis_horse_number > 1:
       change_axis_horse(axis_horse_number)

   #tableの更新
   time.sleep(1)
   table = browser.find_element_by_xpath("/html/body[@id='race_top']/div[@id='page']/div[@class='RaceColumn02']/div[@class='UmarenWrapper clearfix']/div[@id='odds_view_form']/div[@class='W1100']/div[@class='GraphOdds  Grid8 GraphOdds_02 clearfix']")

   odds_id_list = create_odds_id(axis_horse_number)
   odds_list = create_odds_list(odds_id_list)
   odds_all_list.update(odds_list)
   time.sleep(1)


horse_list = ['01','02','03','04','05','06','07','08',
              '09','10','11','12','13','14','15','16']

# error
total1,total2,total3 = [0]*16

for key,value in odds_all_list.items():
   value = float(value)
   tyaku_1 = int(key[:2])
   tyaku_2 = int(key[2:4])
   tyaku_3 = int(key[4:6])
   
   total1[tyaku_1-1] += value
   total2[tyaku_2-1] += value
   total3[tyaku_3-1] += value


total1_dict = dict(zip(horse_list, total1))
total2_dict = dict(zip(horse_list, total2))
total3_dict = dict(zip(horse_list, total3))

total1_sorted = sorted(total1_dict.items(), key=lambda x:x[1])
total2_sorted = sorted(total2_dict.items(), key=lambda x:x[1])
total3_sorted = sorted(total3_dict.items(), key=lambda x:x[1])

df1 = pd.DataFrame(total1_sorted,columns=['1着馬番','1着オッズ'])
df2 = pd.DataFrame(total2_sorted,columns=['2着馬番','2着オッズ'])
df3 = pd.DataFrame(total3_sorted,columns=['3着馬番','3着オッズ'])

df = df1.join([df2, df3])
df['馬番'] = np.arange(1, len(df)+1)
