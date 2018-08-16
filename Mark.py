a=input('请输入去年成绩:')
b=input('请输入今年成绩:')
s1=int(a)
s2=int(b)
r=(s2-s1)/s1*100
print('{0}你的成绩提高了：{1:.1f}%'.format('恭喜',r))
