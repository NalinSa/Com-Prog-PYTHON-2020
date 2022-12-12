x = input()
if len(x) == 10:
    if x[:2:]=='06':
        print('Mobile number')
    elif x[:2:] == '08' :
        print('Mobile number')
    elif x[:2:] == '09' :
        print('Mobile number')
    else:
        print('Not a mobile number')
else:
    print('Not a mobile number')