n = int(input().strip())
dic = {}
for i in range(n):
    x,y = input().split()
    dic[x] = y
    dic[y] = x
nn = int(input())
for i in range(nn):
    z = input()
    if z in dic:
        print(dic[z])
    else: print('Not found')