n = int(input())
a = [0]*n
b = [0]*n
for i in range(n):
    x = [int(e) for e in input().split()]
    a[i] = x[int(i%2!=0)]
    b[i] = x[int(i%2==0)]
zz = input()
if zz == 'Zig-Zag':
    minimum = min(a)
    maxx = max(b)
else :
    minimum = min(b)
    maxx = max(a)
print(minimum, maxx)