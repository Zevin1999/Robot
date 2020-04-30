import go as chicken
import order
#出场
robot_name = '鸡仔'
chicken.show_icon(robot_name)
#询问姓名年龄
name = chicken.ask()

while(True):
	print("鸡仔：你有什么吩咐？")
	cmd = input()
	if(cmd == "time"):
		order.show_time()
	elif(cmd == "hello"):
		order.hello(name,robot_name)
	elif(cmd == 'tianqi'):
		order.tianqi('西安')
	elif(cmd == "88"):
		print("鸡仔：88咯")
		break
	else:
		print(order.ai_talk(cmd))
	print("---------------------------------")
