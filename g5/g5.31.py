x = input().split()
y = input()
c = int(len(x)/2)
for e in y:
    if e == 'C':
        x = x[c::] + x[:c:]
    if e == 'S':
        z = [0]*len(x)
        z[::2] = x[:c:]
        z[1::2] = x[c::]
        x = list(z)
print(' '.join(x))