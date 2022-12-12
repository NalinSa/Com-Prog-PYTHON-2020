n = int(input())
dic = {}
setname = set()
for i in range(n):
    x = input().split()
    setname.add(x[1])
    if x[0] == 'B':
        if x[2] in dic:
            dic[x[2]].append((x[1],int(x[3])))
        else:
            dic[x[2]] = [(x[1],int(x[3]))]
    elif x[0]=='W':
        if x[2] in dic:
            lis = list(dic[x[2]])
            for b,n in lis:
                if x[1] == b:
                    dic[x[2]].remove((b,n))
dicpay = {}
for key in dic:
    l = dic[key]
    nmax = 0
    namax = ''
    for b,n in l:
        if n>nmax:
            nmax = n
            namax = b
    if namax in dicpay:
        dicpay[namax].append((key,nmax))
    else:
        dicpay[namax] = [(key,nmax)]
for name in sorted(setname):
    if name in dicpay:
        s = 0
        lpay = []
        for od,co in dicpay[name]:
            s += co
            lpay.append(od)
        lpay.sort()
        print(name+': $'+str(s)+' -> '+' '.join(lpay)
)
            
    else:
        print(name+': $0')