from selenium import webdriver #web driver をインポート。selenium単体では操作負荷なのでドライバを使用
from selenium.webdriver.common.by import By #Byをインポート
from selenium.webdriver.support.ui import Select

import time 

driver = webdriver.Chrome()#ブラウザ用オブジェクト　今回はchormeをdriver変数に代入　
driver.get("https://www.data.jma.go.jp/risk/obsdl/index.php") #スクレイピング対象のリンク先URL
driver.implicitly_wait(3)

time.sleep(1)

#「東京」をクリック
btn_tokyo_1 = driver.find_element(By.ID,"pr44")
btn_tokyo_1.click()
btn_tokyo_2 = driver.find_element(By.CSS_SELECTOR,"#stationMap > div:nth-child(10)")
btn_tokyo_2.click()


#「項目を選ぶ」をクリック
btn_element = driver.find_element(By.ID, "elementButton")  #ID属性で要素を指定する(今回はelementButton)
btn_element.click()  #クリック要素呼出で対象の要素をクリックする

#「日別値」-「日平均気温」をクリック
radio_by_day = driver.find_element(
    By.CSS_SELECTOR,
    "#aggrgPeriod > div div:nth-child(1) > div:nth-child(2) > label input[type=radio]")
radio_by_day.click()
radio_temp = driver.find_element(By.ID,"平均気温")
radio_temp.click()


#「期間を選ぶ」をクリック
btn_period = driver.find_element(By.ID, "periodButton")  #ID属性で要素を指定する(今回はelementButton)
btn_period.click()  #クリック要素呼出で対象の要素をクリックする

#開始の年
pull_down_ini_y = driver.find_element(By.NAME,"iniy")
Select(pull_down_ini_y).select_by_visible_text("2024")

pull_down_ini_m = driver.find_element(By.NAME,"inim")
Select(pull_down_ini_m).select_by_visible_text("1")

pull_down_ini_d = driver.find_element(By.NAME,"inid")
Select(pull_down_ini_d).select_by_visible_text("1")

#終了の年月日
pull_down_end_y = driver.find_element(By.NAME,"endy")
Select(pull_down_end_y).select_by_visible_text("2024")

pull_down_end_m = driver.find_element(By.NAME,"endm")
Select(pull_down_end_m).select_by_visible_text("1")

pull_down_end_d = driver.find_element(By.NAME,"endd")
Select(pull_down_end_d).select_by_visible_text("10")


#画面に表示」をクリック
bnt_display = driver.find_element(By.CSS_SELECTOR,"#loadTable > img") 
bnt_display.click() 

table_left = driver.find_element(By.CLASS_NAME,"grid-canvas-left")
table_right = driver.find_element(By.CLASS_NAME,"grid-canvas-right")

dates = table_left.find_elements(By.CLASS_NAME,"slick-cell")
temps =  table_right.find_elements(By.CLASS_NAME,"slick-cell")

for d, t in zip(dates, temps):
    print(f"{d.text} : {t.text}度")

time.sleep(2)
driver.quit() #webドライバーの終了






