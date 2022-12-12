x = input().strip()
t = []
while x != 'end':
    t.append(x)
    x = input().strip()
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = A.lower()
for sen in t:
    p = ''
    for i in sen:
        if i in A:
            j = A.find(i)
            p += A[j+13]
        elif i in a:
            j = a.find(i)
            p += a[j+13]
        else: p += i
    print(p)
        