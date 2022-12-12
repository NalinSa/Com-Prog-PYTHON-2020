x = input()
y = ['0','1','2','3','4','5','6','7','8','9']
for e in x:
    if e in y:
        y.remove(e)
if y == []:
    y.append('None')
print(','.join(y))