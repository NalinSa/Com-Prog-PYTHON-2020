x = [int(e) for e in input().split()]
x.sort()
c = 1
y = []
for i in range(len(x)-1):
    if x[i]!=x[i+1]:
        c += 1
for e in x:
    if e not in y:
        y.append(e)
print(c)
print(y[:10:])
        
    