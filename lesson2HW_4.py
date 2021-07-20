math=input('數學成績?')
math=int(math)
Eng=input('英文成績?')
Eng=int(Eng)

if math>=90 and Eng>=90:
    print('有獎品')
elif math<60 and Eng<60:
    print('要處罰')
elif math<60 or Eng<60:
    print('加油')
else:
    print('ok')
    
