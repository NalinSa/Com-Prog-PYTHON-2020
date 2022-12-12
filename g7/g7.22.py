x = input().lower().split()
y = input().lower().split()
w1 = ''.join(x)
w2 = ''.join(y)
al1 = []
al2 = []
for e in w1:
    if e not in al1:
        al1.append(e)
for e in w2:
    if e not in al2:
        al2.append(e)
al1.sort()
al2.sort()
c1 = [0]*len(al1)
c2 = [0]*len(al2)
for i in w1:
    x = al1.index(i)
    c1[x] += 1
for i in w2:
    x = al2.index(i)
    c2[x] += 1
if al1 == al2 and c1 == c2:
    print('YES')
else: print('NO')