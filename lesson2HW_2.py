score=input('成績?')
score=int(score)
if score<60:
    print('抱歉,不及格')
else:
    print('恭喜,''及格')

if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')
    