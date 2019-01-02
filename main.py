print('Welcome to my Calculator')
a=float(input('Enter 1st Number:'))
b=float(input('Enter 2nd Number:'))
print("add,mul,sub,div")
c=input("enter what do you want and type as shown above line:")
if (c == 'add'):
    print('here your result' ,a, '+', b, "=", a+b)
if (c=='mul'):
    print('here your result' ,a, '*', b, "=", a*b)
if (c=='sub'):
    print('here your result' ,a, '-', b, "=", a-b)
if (c=='div'):
    print('here your result' ,a, '/', b, "=", a/b)
