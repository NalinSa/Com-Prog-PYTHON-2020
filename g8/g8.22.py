n = int(input())
dic = {}
for i in range(n):
    name,count = input().split()
    dic[name] = float(count)
sale = {}
for key in dic:
    sale[key] = 0
nn = int(input())
for i in range(nn):
    n,c = input().split()
    if n in sale:
        sale[n] += float(c)
total = 0
lis = []
for e in sale:
    sale[e] *= dic[e]
    total += sale[e]
    lis.append([-sale[e],e])
lis.sort()
top = []
for sale,na in lis:
    if sale == lis[0][0]:
        top.append(na)
Top = ', '.join(top)
if total != 0:
    print('Total ice cream sales:',total)
    print('Top sales:',Top)
else:
    print('No ice cream sales')