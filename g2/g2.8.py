import math
x = input().split(',')
b = int('9'*len(x[2])+'0'*len(x[1]))
a = int(x[1]+x[2])-int(x[1]+'0')//10+int(x[0])*b
c = math.gcd(a,b)
print(int(a//c),'/',int(b//c))