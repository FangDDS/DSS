a = input('请输入您的身高：')
h1 = float(a)
b = input('请输入您的体重: ')
w1 = float(b)
BMI = w1/(h1*h1)
print('{0}健康指数为：{1:.1f}' .format('您的',BMI))
if BMI >= 32:
	print('做一个幸福的胖子吧')
elif BMI >= 28:
	print('啧啧啧，在不锻炼就没人要啦')
elif BMI >= 25:
	print('需要注意饮食咯')
elif BMI >= 18.5:
	print('健康身体')
else:
	print('瘦成闪电')

