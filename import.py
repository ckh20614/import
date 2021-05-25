#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出 '你猜對了!'
#猜錯的話 要告訴他 比答案大or小

import random
start = input('請設定範圍開始值')
end = input('請設定範圍結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1  #也可寫成count += 1
	num = input('猜的數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')		