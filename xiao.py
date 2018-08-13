a = input('去年成绩：')
b = input('今年成绩: ')
s1 = int(a)
s2 = int(b)
r = (s1-s2)/s1*100
print('{0}成绩是:{1:.1f}%'.format('小明',r))