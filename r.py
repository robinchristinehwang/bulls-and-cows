import random #standard library, 

r = random.randint(1,100) #隨機整數
while True:
	a = input('請選數字')
	a = int(a)
	if a == r:
		print('你猜對了!')
		break
	else:
		print('請繼續猜!')
		if a <= r:
			print('要再大一點!')
		else:
			print('要再小一點!')



