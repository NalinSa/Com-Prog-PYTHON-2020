lis = []
n = int(input())
for i in range(n):
    x = input().strip().split()
    lis.append([x[0],x[1],x[2],x[3]])
y = input().strip().split()
l = []
for a in lis:
    if set(y) <= set(a[1::]):
        l.append(a)
if len(l) == 0:
    print('Not Found')
else:
    for u in sorted(l):
        print(' '.join(u))