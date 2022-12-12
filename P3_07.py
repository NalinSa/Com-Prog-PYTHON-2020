n = int(input())
dic = {}
for i in range(n):
    x = input()
    y = input().split()
    dic[x] = y
word = input()
while word != '-1':
    l = []
    for key in dic:
        on = dic[key].count(word)
        tw = len(dic[key])
        th = len(set(dic[key]))
        cal = on/tw/th
        l.append([cal,key])
    l.sort()
    if l[-1][0] != 0:
        print(l[-1][1])
    else: print('Not found'.upper())
    word = input()
    