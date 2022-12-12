def reverse(d):
    re = {}
    for key in d:
        re[d[key]] = key
    return re
def keys(d,v):
    lis = []
    for key in d:
        if d[key] == v:
            lis.append(key)
    return lis

print(reverse({3:"A",2:"B"}) == {"A":3,"B":2})