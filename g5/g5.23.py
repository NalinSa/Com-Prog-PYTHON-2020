n = int(input())
c = []
for i in range(n):
    x = input().split()
    c.append([i+1,float(x[0]),float(x[1])])
c1 = []
for e in c:
    dis = ((e[1])**2+(e[2])**2)**0.5
    c1.append([dis, e[0], e[1], e[2]])
c1.sort()
y = c1[2]
print('#'+str(y[1])+': ('+str(y[2])+', '+str(y[3])+')')