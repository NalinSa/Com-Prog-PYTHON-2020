x = input()
vobnk = {}
nvota = {}
kami = {}
while x not in ['1','2','3']:
    ota,bnk,vote = x.split()
    vote = int(vote)
    if ota in kami:
        if vote>kami[ota][1]:
            kami[ota] = [bnk,vote]
        elif vote==kami[ota][1]:
            if bnk<kami[ota][0]:
                kami[ota] = [bnk,vote]                
    else:
        kami[ota] = [bnk,vote]
    if bnk in vobnk:
        vobnk[bnk]+= vote
    else:
        vobnk[bnk] = vote
    if bnk in nvota:
        nvota[bnk].add(ota)
    else:
        nvota[bnk] ={ota}
    x = input()
if x == '1':
    l = []
    for key in vobnk:
        l.append([vobnk[key],key])
    l.sort()
    print(l[-1][1]+', '+l[-2][1]+', '+l[-3][1])
elif x== '2':
    l = []
    for key in nvota:
        l.append([len(nvota[key]),key])
    l.sort()
    print(l[-1][1]+', '+l[-2][1]+', '+l[-3][1])
elif x=='3':
    lnamebnk = sorted(nvota)
    lkami = sorted(kami.values())
    nn = []
    for a,b in lkami:
        nn.append(a)
    l = []
    for name in lnamebnk:
        l.append([nn.count(name),name])
    l.sort()
    print(l[-1][1]+', '+l[-2][1]+', '+l[-3][1])
        
    