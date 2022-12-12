n = int(input())
dic = {}
for i in range(n):
    x = input().split()
    dic[x[0]] = [0]*int(x[1])   
m = int(input())
lis = []
for i in range(m):
    x = input().split()
    lis.append([float(x[1]),x[2::],x[0]])
lis.sort()
for e in lis[::-1]:
    for k in e[1]:
        if 0 in dic[k]:
            index = dic[k].index(0)
            dic[k][index] = e[-1]
            break
lislis = []
for key in dic:
    for e in dic[key]:
        if e != 0:
            lislis.append([e,key])
lislis.sort()
for a,b in lislis:
    print(a,b)