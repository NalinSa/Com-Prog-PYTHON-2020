x = int(input())
if x >= 10**10 :
    x += 5*10**8
    y = x//10**9
    print(str(y)+'B')
elif x >= 10**9 :
    x /= 10**9
    y = round(x,1)
    print(str(y)+'B')
elif x >= 10**7 :
    x += 5*10**5
    y = x//10**6
    print(str(y)+'M')
elif x >= 10**6 :
    x /= 10**6
    y = round(x,1)
    print(str(y)+'M')
elif x >= 10**4 :
    x += 5*10**2
    y = x//10**3
    print(str(y)+'K')
elif x >= 10**3 :
    x /= 10**3
    y = round(x,1)
    print(str(y)+'K')
else:
    print(x)