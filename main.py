print('Welcome to my Calculator')
a=float(input('Enter 1st Number:'))
b=float(input('Enter 2nd Number:'))
print("add,mul,sub,div")
c=input("enter what do you want and type as shown above line:")
if (c == 'add'):
    z=a+b
    print('here your result' ,a, '+', b, "=", z)
if (c=='mul'):
    z=a*b
    print('here your result' ,a, '*', b, "=", z)
if (c=='sub'):
    z=a-b
    print('here your result' ,a, '-', b, "=", z)
if (c=='div'):
    try:
        z=a/b
    except Exception as e:
        z=None
print('here your result' ,a, '/', b, "=", z)
