from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import requests
import datetime
import time

driver = webdriver.Chrome('/Users/andoushouta/Downloads/chromedriver 3')
error_flg = False
target_url = 'https://portal.mc.chitose.ac.jp/portal/'
driver.get(target_url)  
sleep(3)

if error_flg is False:
    try:
        f = open('data5.txt')  # f = open('test.txt', 'rt'):
        b = f.read()  # ファイルの全内容が1つの文字列として返される
        username_input = driver.find_element_by_xpath('//input[@id="userID"]')
        username_input.send_keys(b)
        f.close()
        sleep(1)
 
        f = open('data4.txt')  # f = open('test.txt', 'rt'):
        a = f.read()  # ファイルの全内容が1つの文字列として返される
        password_input = driver.find_element_by_xpath('//input[@id="password"]')
        password_input.send_keys(a)
        f.close()
        sleep(1)
 
        username_input.submit()
        sleep(1)
        
    except Exception:
        print('ユーザー名、パスワード入力時にエラーが発生しました。')
        error_flg = True
try:
    login_button = driver.find_element_by_link_text('ログイン')
    login_button.click()
    sleep(3)
except Exception:
    error_flg = True
    print('ログインボタン押下時にエラーが発生しました。')
if error_flg is True: #True?
    try:
        login_button = driver.find_element_by_link_text('授業')
        login_button.click()

    except Exception:
        print("error")
        pass
if error_flg is True: #True?
    try:
        # テキストファイルをオープンして、その内容を全て読み込み、クローズする
        f = open('data1.txt')  # f = open('test.txt', 'rt'):
        s = f.read()  # ファイルの全内容が1つの文字列として返される
            
        login_button = driver.find_element_by_link_text(s) 
        login_button.click()

    except Exception:
        print("error")
        pass

if error_flg is True:
  
        try:
            dropdown = driver.find_element_by_name('lectureSelector')
            select = Select(dropdown) 
            # テキストファイルをオープンして、その内容を全て読み込み、クローズする
            f = open('data2.txt')  # f = open('test.txt', 'rt'):
            t = f.read()  # ファイルの全内容が1つの文字列として返される
                      
            select.select_by_value(t) 
            sleep(3)
            login_button = driver.find_element_by_id('id1c').click()
            sleep(3)
            times = driver.find_element_by_xpath("//dl[@class='well']")

            def line(ms_data,url,token):
                post_data = {'message': ms_data}
                headers = {'Authorization': 'Bearer ' + token}
                #送信
                res = requests.post(url,data=post_data,headers=headers)
                print(res.text)#メッセージが送信されたかどうかの確認
            token = ''
            url = 'https://notify-api.line.me/api/notify'#LINE NotifyのAPIのURL
            ms = s +"\n"+ times.text#送信するメッセージ
 
            while True:
                dt = datetime.datetime.now()#現在時刻の取得
                f = open('data3.txt')  # f = open('test.txt', 'rt'):
                u = f.read()  # ファイルの全内容が1つの文字列として返される        

                now=dt.strftime('%Y-%m-%d-%H:%M')    #自分で好きなときに通知できるようにしたい（Websサイトで？）
                if now == u  :#時刻の指定
                    sleep(3)
                    line(ms + now,url,token)#自作関数lineを呼び出す
                    break
                f.close()
                time.sleep(1)

        except Exception:
            def line(ms_data,url,token):
                post_data = {'message': ms_data}
                headers = {'Authorization': 'Bearer ' + token}
                #送信
                res = requests.post(url,data=post_data,headers=headers)
                print(res.text)#メッセージが送信されたかどうかの確認
            token = ''
            url = 'https://notify-api.line.me/api/notify'#LINE NotifyのAPIのURL
            ms = s +"\n今回は課題ありません"
 
            while True:
                dt = datetime.datetime.now()#現在時刻の取得
                f = open('data3.txt')  # f = open('test.txt', 'rt'):
                u = f.read()  # ファイルの全内容が1つの文字列として返される        

                now=dt.strftime('%Y-%m-%d-%H:%M')    #自分で好きなときに通知できるようにしたい（Websサイトで？）
                if now == u  :#時刻の指定
                    sleep(3)
                    line(ms + now,url,token)#自作関数lineを呼び出す
                    break
                f.close()
                time.sleep(1)
            pass

