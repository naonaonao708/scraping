import selenium
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.support.select import Select

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
   