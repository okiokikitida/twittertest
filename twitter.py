
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import time

# USERにアカウント名を入力、PASSにパスワード入力してください。
USER = "Adriana96490814"
PASS = "kLuRIiVR9VvYorf"

#ブラウザ起動
browser = webdriver.Chrome()
browser.implicitly_wait(5)

#サイトアクセス
url_login = "https://twitter.com/login"
browser.get(url_login)
time.sleep(3)
print("アクセス完了")

name_path = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
pass_path = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
btn_path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'

# ログイン情報入力
element = browser.find_element_by_xpath(name_path)
element.clear()
element.send_keys(USER)
element = browser.find_element_by_xpath(pass_path)
element.clear()
element.send_keys(PASS)
print("フォームを送信")

# ログイン実行
browser_from = browser.find_element_by_xpath(btn_path)
time.sleep(3)
browser_from.click()
print('情報を入力してログインボタンを押しました')

# 国、言語指定
setting_url = 'https://twitter.com/settings/your_twitter_data/account'
browser.get(setting_url)
try:
    element = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/label/div/div[2]/div/input')
    element.clear()
    element.send_keys(PASS)
    browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[4]/div/div')
    browser_select.click()
except:
    print('要素なし')
    pass
# 国選択
time.sleep(2)
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[5]')
browser_select.click()
time.sleep(1)
dropdown = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div/div[1]/select')
select = Select(dropdown)
select.select_by_value('jp')
browser.back()
time.sleep(1)
# 言語選択
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[6]')
browser_select.click()
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/a[1]')
browser_select.click()
time.sleep(2)
dropdown = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div/div[1]/select')
select = Select(dropdown)
select.select_by_value('ja')
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div/div')
browser_select.click()
browser.back()
time.sleep(1)

# コンテンツ設定
setting_url = 'https://twitter.com/settings/privacy_and_safety'
browser.get(setting_url)
# センシティブツイートOFF
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[2]')
browser_select.click()
time.sleep(1)
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
select_judge = browser_select.is_selected()
if select_judge == True:
    browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
    browser_select.click()
    browser.back()
else:
    browser.back()
time.sleep(1)
# センシティブ表示ON
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[3]')
browser_select.click()
time.sleep(1)
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
select_judge = browser_select.is_selected()
if select_judge == True:
    pass
else:
    browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
    browser_select.click()
time.sleep(1)
# センシティブ検索OFF
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/a[4]')
browser_select.click()
time.sleep(1)
browser_select = browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/label/div[2]/input')
select_judge = browser_select.is_selected()
if select_judge == True:
    browser_select = browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/label/div[2]/input')
    browser_select.click()
    browser.get(setting_url)
else:
    pass
    browser.get(setting_url)
time.sleep(1)
# ダイレクトメッセージOFF
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[5]')
browser_select.click()
time.sleep(1)
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
select_judge = browser_select.is_selected()
if select_judge == True:
    browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
    browser_select.click()
else:
    pass
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/label/div[2]/input')
select_judge = browser_select.is_selected()
if select_judge == True:
    browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/label/div[2]/input')
    browser_select.click()
else:
    pass
time.sleep(1)
# クオリティフィルターOFF
setting_url = 'https://twitter.com/settings/notifications'
browser.get(setting_url)
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/a[1]')
browser_select.click()
time.sleep(1)
browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
select_judge = browser_select.is_selected()
if select_judge == True:
    browser_select = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[2]/label/div[2]/input')
    browser_select.click()
else:
    pass
time.sleep(1)
setting_url = 'https://twitter.com/home'
browser.get(setting_url)


