# 測驗紙
import random
start = input('請輸入開始值：')
end = input('請輸入結束值：')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('恭喜猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('答案比', num, '小')
	elif num < r:
		print('答案比', num, '大')
	print('這是你猜的第', count, '次')
