a=int(input("Введіть перше число:"))
b= int(input("Введіть друге число:"))
c= input("Вибери дію:(+,-,*,/)")
if c=='+' :
    print('Результат:' , a+b)
elif c=='-':
    print('Результат:' , a-b)
elif c=='*':
    print('Результат:' , a*b)
elif c=='/':
    print('Результат:' , a/b)
else: print("Не правильна операція")