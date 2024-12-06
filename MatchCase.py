x=int(input('Enter the Value of X:'))
match x:
    case 0:
        print('x is Zero')
    case 4:
        print('case is 4')
    case _ if x!=50:
        print(x,'is not 50')
    case _ if x!=40:
        print(x,'is not 40')
    case _:
        print(x)