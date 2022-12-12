x = input().split()
c = []
while x != ['q']:
    c += x 
    x = input().split()
i = c[0::2]
g = c[1::2]
ri = input().split()
for e in ri:
    if e in i:
        y = i.index(e)
        if g[y] == 'B+':
            g[y] = 'A'
        elif g[y] == 'B':
            g[y] = 'B+'
        elif g[y] == 'C+':
            g[y] = 'B'
        elif g[y] == 'C':
            g[y] = 'C+'
        elif g[y] == 'D+':
            g[y] = 'C'
        elif g[y] == 'D':
            g[y] = 'D+'
        elif g[y] == 'F':
            g[y] = 'D'
c[0::2],c[1::2] = i,g
d = []
for i in range(0,len(c)-1,2):
    d.append([c[i],c[i+1]])
d.sort()
for num,grade in d:
    print(num, grade)