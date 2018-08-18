a = input('请输入您的身高：')
b = input('请输入您的体重: ')
s = input('请输入出生年：')
	h = float(a)
	w = float(b)
BMI = (h*h)/w*1000
	d = int(s)
if d > 2000:
	print('00后')
else:
	print('00前')
print('{0}健康指数为：{1:.2f}' .format('您的',BMI))
if BMI >= 32:
	print('做一个幸福的胖子吧')
elif BMI >= 28:
	print('啧啧啧，在不锻炼就没人要啦')
elif BMI >= 25:
	print('需要注意饮食咯')
elif BMI >= 18.5:
	print('完美身材')
else:
	print('瘦成闪电')

