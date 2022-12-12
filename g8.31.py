def total(pocket):
    s = 0
    for key in pocket:
        s += key*pocket[key]
    return s 
        
def take(pocket, money_in):
    for key in money_in:
        if key in pocket:
            pocket[key] += money_in[key]
        else:
            pocket[key] = money_in[key]

def pay(pocket, amt):
    y = dict(pocket)
    x = sorted(pocket)[::-1]
    j = 0
    t = False
    dic = {}
    while amt>0:
        r = 0
        for key in pocket:
            if key <= amt:
                r += pocket[key]
        if r == 0:
            t = True
            break
        if x[j]>amt:
            j += 1
        else:
            if pocket[x[j]]>0:
                amt -= x[j]
                pocket[x[j]] -= 1
                if x[j] in dic:
                    dic[x[j]] += 1
                else:
                    dic[x[j]] = 1
            else:
                j += 1
    if t:
        for key in y:
            pocket[key] = y[key]
        return {}
    else:
        return dic
p={10:5, 1:7};print(pay(p, 18));print(p)