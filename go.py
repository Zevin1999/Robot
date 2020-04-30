
def show_icon(robot_name):
		print(f'''
	      \_/
	     (* *)
	    __)#(__
	   ( )...( )(_)s
	   || |_| ||//
	>==() | | ()/
	    _(___)_
	   [-]{robot_name}[-]
		''')

def ask():
	# 输入姓名、年龄
	#转义字符
	name = input("What\'s your name ?\n>>>")
	age = input("How old are you？\n>>>")
	# print(id(age))
	#类型转换
	age = int(age)
	# print(id(age))
	#判断
	if(age<18):
		print(f"你才{age}岁,小屁孩！")
	elif(age>=18 and age<30):
		print(f"{age}岁真好！")
	else:
		print(f"{age}岁，且行且珍惜")
	return name

# def run_nian(year):
# 	return (year%4==0 and year%100!=0) or year%400==0

# #断言:测试用例
# assert run_nian(2005)==False
# assert run_nian(2000)==True
