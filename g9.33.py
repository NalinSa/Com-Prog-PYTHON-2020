def add_poly(p1, p2):
    dic = {}
    for a,x in p1:
        dic[x] = a
    for b,y in p2:
        if y in dic:
            dic[y] += b
        else:
            dic[y] = b
    lis = []
    for key in sorted(dic)[::-1]:
        if dic[key] != 0:
            lis.append((dic[key],key))
    return lis

def mult_poly(p1, p2):
    dic = {}
    for a,x in p1:
        for b,y in p2:
            nu = a*b
            xx = x+y
            if xx in dic:
                dic[xx] += nu
            else:
                dic[xx] = nu
    lis = []
    for key in sorted(dic)[::-1]:
        if dic[key] != 0:
            lis.append((dic[key],key))
    return lis   

for i in range(3):
    exec(input().strip())