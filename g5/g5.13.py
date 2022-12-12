r = []
n = int(input())
for a in range(n):
    x = int(input())
    r.append(x)
o =[int(e) for e in input().split()]
r += o
p = int(input())
while p != -1:
    r.append(p)
    p = int(input())
t = []
for i in range(len(r)):
    if i%2 == 0:      
        t.append(r[i])
    else:
        t.insert(0,r[i])
print(r)
print(t)