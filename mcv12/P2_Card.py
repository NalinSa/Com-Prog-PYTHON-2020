x = input().strip()
l = ''
p1 = [' ','A', '2', '3', '4' ,'5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
p2 = [' ', 'C', 'D', 'H','S']
for i in range(0,len(x)-2,2):
    a = x[i:i+2]
    b = x[i+2:i+4]
    if a[0]==b[0]:
        nu = p2.index(a[1])-p2.index(b[1])
        if nu>0:
            l += '+'
        l += str(nu)
    else:
        nu = p1.index(a[0])-p1.index(b[0])
        if nu>0:
            l += '+'
        l += str(nu)
print(l)
    