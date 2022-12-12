x = input().split()
maxxa = int(x[0])
minna = int(x[0])
maxxb = int(x[1])
minnb = int(x[1])
i = 0
while i >= 0:
    i += 1
    x = input().split()
    if 'Zig-Zag' in x or 'Zag-Zig' in x: break
    a = int(x[int(i%2!=0)])
    if a > maxxa:
        maxxa = a
    else:
        if a < minna:
            minna = a
    b = int(x[int(i%2==0)])
    if b > maxxb:
        maxxb = b
    else:
        if b < minnb:
            minnb = b
if 'Zig-Zag' in x:
    print(minna,maxxb)
elif 'Zag-Zig' in x:
    print(minnb,maxxa)