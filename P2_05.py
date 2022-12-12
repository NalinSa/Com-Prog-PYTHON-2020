a = input()
b = input()
la = []
lb  = []
for e in a:
    if 'a'<=e.lower()<='z':
        la.append(e.lower())
for e in b:
    if 'a'<=e.lower()<='z':
        lb.append(e.lower())
lisa= list(la)
lisb= list(lb)
for e in lisa:
    if e in la and e in lb:
        la.remove(e)
        lb.remove(e)
da = {}
for e in la:
    if e in da:
        da[e] += 1
    else:
        da[e] = 1
db = {}
for e in lb:
    if e in db:
        db[e] += 1
    else:
        db[e] = 1
print(a)
if len(da) == 0:
    print(' - None')
else:
    for key in sorted(da):
        if da[key]>1:
            print(' - remove',str(da[key]),key+'\'s')
        else:
            print(' - remove',str(da[key]),key)
print(b)
if len(db) == 0:
    print(' - None')
else:
    for key in sorted(db):
        if db[key]>1:
            print(' - remove',str(db[key]),key+'\'s')
        else:
            print(' - remove',str(db[key]),key)