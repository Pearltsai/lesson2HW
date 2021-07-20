math=input('數學成績?')
math=int(math)
Eng=input('英文成績?')
Eng=int(Eng)

if math>=90 and Eng>=90:
    print('有獎學金')
elif math==100 or Eng==100:
    print('有獎學金')
else:
    print('沒獎學金')
    