x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
if a>b:
    a,b = b,a
    if d>= a:
        if c > d :
            c -= a
    else :
        c += a
    b = a+c+d
elif c> a >= b :
    d += a
if d>c :
    b += 2
else:
    b *= 2
print(a,b,c,d)
