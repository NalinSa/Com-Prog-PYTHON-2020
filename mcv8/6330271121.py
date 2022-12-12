# Prog-08: Bag-of-words
# 6330271121 Nalin Baipluthong
file_name = input('File name = ')
ufh = input('Use feature hashing ? (y,Y,n,N) ').lower()

while ufh not in ['y','n']:
    print('Try again.')
    ufh = input('Use feature hashing ? (y,Y,n,N) ').lower()
    
stopword = open('stopwords.txt')
stw = []
for line in stopword:
    sword = line.strip().lower().split()
    stw += sword
stopword.close()

if ufh == 'n':
    fin = open(file_name)
    charc = 0
    alphc = 0
    linec = 0
    wordc = 0
    all_words = []
    cutwords = []
    for line in fin:
        linec += 1
        line = line.lower()
        if line[-1] == '\n':
            line = line[0:-1:1]
        charc += len(line) 
        newlin = '' 
        for e in line:
            if e in 'abcdefghijklmnopqrstuvwxyz' or e in '1234567890':
                newlin += e
            else:
                newlin += ' '
        words = newlin.split()
        all_words +=  words
        for a in words:
            if a not in cutwords and a not in stw:
                cutwords.append(a)
        al = ''.join(words)
        alphc += len(al)
        wordc += len(words)
    print('-------------------')
    print('char count =',charc)
    print('alphanumeric count =',alphc)
    print('line count =',linec)
    print('word count =',wordc)
    cutwords.sort()
    c = [0]*len(cutwords)
    for i in all_words:
        if i in cutwords:
            j = cutwords.index(i)
            c[j] += 1
    bow = []
    for i in range(len(c)):
        bow.append([cutwords[i],c[i]])        
    fin.close()
    print('BoW =',bow)

def fhash(w,M):
    num = 0
    for i in range(len(w)):
        num += ord(w[i])*(37**i)
    fhash = num%M
    return fhash
    
if ufh == 'y':
    M = int(input('M = '))
    fin = open(file_name)
    charc = 0
    alphc = 0
    linec = 0
    wordc = 0
    cutwords = []
    for line in fin:
        linec += 1
        line = line.lower()
        if line[-1] == '\n':
            line = line[0:-1:1]
        charc += len(line) 
        newlin = ''
        for e in line:
            if e in 'abcdefghijklmnopqrstuvwxyz' or e in '1234567890':
                newlin += e
            else:
                newlin += ' '
        words = newlin.split()
        for a in words:
            if a not in stw:
                cutwords.append(a)
        al = ''.join(words)
        alphc += len(al)
        wordc += len(words)
    print('-------------------')
    print('char count =',charc)
    print('alphanumeric count =',alphc)
    print('line count =',linec)
    print('word count =',wordc)
    fh = []
    for o in cutwords:
        if fhash(o,M) not in fh:
            fh.append(fhash(o,M))
    fh.sort()
    c = [0]*len(fh)
    for u in cutwords:
        j = fh.index(fhash(u,M))
        c[j] += 1
    bow = []
    for i in range(len(c)):
        bow.append([fh[i],c[i]])        
    fin.close()
    print('BoW =',bow)