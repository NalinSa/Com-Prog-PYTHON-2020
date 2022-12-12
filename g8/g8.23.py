n = int(input())
dic = {}
for i in range(n):
    x,z,y = input().split()
    dic[x+' '+z] = y
    dic[y] = x+' '+z
nn = int(input())
for i in range(nn):
    z = input()
    if z in dic:
        print(z,'-->',dic[z])
    else:
        print(z,'-->','Not found')