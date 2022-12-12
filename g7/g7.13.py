x = input().strip().lower()
y = ''
for e in x:
    if e in '-;:\'()[]{}/\\,.\"><':
        y += ' '
    else: y += e
z = y.split()
t = [z[0][0].lower()+z[0][1::]]
for a in z[1::]:
    a0 = a[0].upper()
    a = a0 + a[1::]
    t.append(a)
print(''.join(t))