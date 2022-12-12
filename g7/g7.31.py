dna = input().strip().lower()
ope = input().lower()
t = True
for e in dna:
    if e not in 'atcg':
        t = False
        print('Invalid DNA')
if ope == 'r' and t:
    dn = ''
    for e in dna:
        if e == 'a':
            dn += 't'
        if e == 'c':
            dn += 'g'
        if e == 'g':
            dn += 'c'
        if e == 't':
            dn += 'a'
    red = dn[::-1].upper()
    print(red)
if ope == 'f' and t:
    new = 'atgc'
    f = [0,0,0,0]
    for e in dna:
        j = new.find(e)
        f[j] += 1
    print('A='+str(f[0])+', '+'T='+str(f[1])+', '+'G='+str(f[2])+', '+'C='+str(f[3]))
if ope == 'd' and t:
    wa = input().strip().lower()
    d = 0
    ser = dna.find(wa)
    while ser != -1:
        d += 1
        jj = ser + 1
        ser = dna.find(wa, jj)
    print(d)