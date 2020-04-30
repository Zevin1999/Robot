from datetime import datetime
import requests
import json
#显示时间
def show_time():
	dt = datetime.now()
	# print(f"现在时刻 {dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}")
	print(dt.strftime("现在时刻%Y-%m-%d %H:%M:%S"))

#问好
def hello(name,robot_name):
	#变量
	print('欢迎',name,'来到',robot_name,'的世界！')
	print('你好,'+name+'!')
	print('我是{}。'.format(robot_name))
	# print('点击链接你也可以找到更多机器人https://www.asciiart.eu/electronics/robots')
	# #分隔符
	# print(1,2,3,4,5,sep="|",end=" ")

#聊天
def ai_talk(question):
	return question.replace('你','我').replace('不','').replace('吗','').replace('?','!').replace('？','！')
#天气预报
#API:Application Programming Interface
#Restful API:基于网页的API
#JSON:JavaScript Notation
def tianqi(city):
	url = "http://t.weather.sojson.com/api/weather/city/101210101"
	res = requests.get(url)
	tq_text = res.text
	tq_json = json.loads(tq_text)
	wendu = tq_json["data"]["wendu"]
	pm25 = tq_json["data"]["pm25"]
	print(f'{city}：温度:{wendu}° pm2.5:{pm25}')