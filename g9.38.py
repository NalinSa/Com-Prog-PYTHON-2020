x = input().split()
dic = {}
while len(x) != 1:
    if x[0] in dic:
        dic[x[0]].append(x[1])
    else:
        dic[x[0]] = [x[1]]
    if x[1] in dic:
        dic[x[1]].append(x[0])
    else:
        dic[x[1]] = [x[0]]
    x = input().split()
l = set()
if x[0] in dic:
    for sta1 in dic[x[0]]:
        l.add(sta1)
        if sta1 in dic:
            for sta2 in dic[sta1]:
                l.add(sta2)          
else:
    l.add(x[0])
[print(i) for i in sorted(l)]