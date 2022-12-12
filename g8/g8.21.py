x = input().lower()
dic = {}
for e in x:
    if 'a'<= e <='z':
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
lis = []
for key in dic:
    lis.append([-dic[key],key])
lis.sort()
for num,al in lis:
    print(al,'->',-num)