# 需要一个web框架
# pip install Flask

from flask import Flask,render_template
from random import randint
app=Flask(__name__) #定义服务器对象
 
jingling=['爵刻·黑沃德','朵特','普达','禅老','流荧·雪',
'露泽莫尔','岭妃','古温婆婆','鱿里子','眠降·玛缇娜','鲨鱼娘',
'闪光猛虎王','厄塔沃姆','银椋·奥雷莫德','查理斯','幽火·海登',
'蛮龙之戟·赫比德','库托里希','谧娜','恶咒巫师·科萨斯']
@app.route('/index')
def index():
    return render_template('index.html',neirong=jingling)
@app.route('/choujiangla')
def choujiangla():
    num=randint(0,len(jingling)-1) #不-1会下标溢出
    return render_template('index.html',neirong=jingling,h=jingling[num])
app.run(debug=True) #启动Flask 加上括号内的东西，
#方便开发，即每次调试不需要重复终止终端
