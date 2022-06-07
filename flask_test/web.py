from flask import Flask, render_template
from flask import request
from selenium.webdriver.support.select import Select
from time import sleep
from flask import Flask
import os

path = 'data1.txt'
is_file = os.path.isfile(path)
if is_file:
    print(f"{path} is a file.")
else:
    pass # パスが存在しないかファイルではない

path2 = 'data2.txt'
is_file = os.path.isfile(path2)
if is_file:
    print(f"{path2} is a file.")
else:
    pass # パスが存在しないかファイルではない

app = Flask(__name__)
 
# トップ画面
@app.route('/')
def index():
    return render_template('index.html')

# post処理の入力フォームを表示
@app.route("/request_post", methods=["GET"])
def post_sample():
    return render_template('send_post.html')


# postでの入力情報処理
@app.route("/request_post", methods=["POST"])
def post_action():
    if 'userID' in request.form.keys():
        userID = request.form['userID']
        f = open('data5.txt', mode='w')
        f.write(userID)
        f.close()
    else:
        student_id = '?'

    if 'password' in request.form.keys():
        password = request.form['password']
        f = open('data4.txt', mode='w')
        f.write(password)
        f.close()
    else:
        password = '?'

    if 'lectureSelector' in request.form.keys():
        lectureSelector_range = request.form['lectureSelector']
        f = open('data1.txt', mode='w')
        f.write(lectureSelector_range)
        f.close()

    else:
        lectureSelector_range = '?'
    
    if 'numberSelector' in request.form.keys():
        numberSelector_range = request.form['numberSelector']
        f = open('data2.txt', mode='w')
        f.write(numberSelector_range )
        f.close()

    else:
        numberSelector_range = '?'

    if 'date' in request.form.keys():
        date_range = request.form['date']
        print(date_range)
        f = open('data3.txt', mode='w')
        f.write(date_range+"-")
        f.close()

    else:
        date_range = '?'

    if 'example1' in request.form.keys():
        example1_range = request.form['example1']
        f = open('data3.txt', mode='a')
        f.write(example1_range )
        f.close()


    else:
        example1_range= '?'
    return f'{lectureSelector_range}{numberSelector_range}回目の課題に関する通知を{date_range}の{example1_range}にします。'
    

# テスト環境起動
app.run(debug=True)