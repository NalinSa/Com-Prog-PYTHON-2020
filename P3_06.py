n = int(input())
dic = {}
for i in range(n):
    x = input().split(',')
    for e in x[1::]:
        if e.strip() in dic:
            dic[e.strip()].append(x[0].strip())
        else:
            dic[e.strip()] = [x[0].strip()]
y = input().split(',')
for q in y:
    l = q.strip()+' -> '
    if q.strip() in dic:
        l += ', '.join(dic[q.strip()])
    else:
        l+='Not found'
    print(l)