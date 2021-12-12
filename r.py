import random #standard library, 

r = random.randint(1,100) #隨機整數
print(r)
while True:
	a = input('請選數字')
	a = int(a)
	if a == r:
		print('你猜對了!')
		break
	else:
		print('請繼續猜!')



