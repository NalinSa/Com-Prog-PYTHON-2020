x1 = input().split(',')
y1 = x1[0].split('[')
z1 = x1[2].split(']')
a = [float(y1[1]), float(x1[1]), float(z1[0])]
x2 = input().split(',')
y2 = x2[0].split('[')
z2 = x2[2].split(']')
b = [float(y2[1]), float(x2[1]), float(z2[0])]
c = [a[0]+b[0], a[1]+b[1], a[2]+b[2]]
print(a,'+',b,'=',c)