x = input().strip()
n = int(input())
p = [0]*10
i = 0
j = 0
while j<9:
    if x[i] == 'X':
        p[j] = 'X'
        i += 1
        j += 1
    elif '0'<=x[i]<='9':
        p[j] = x[i:i+2]
        i += 2
        j += 1
p[9] = x[i:]
s = [0]*10
for i in range(len(p)-1):
    if p[i]=='X':
        s[i]+=10
        plus=p[i+1]
        if len(plus) == 1:
            plus += p[i+2][0]
            for e in plus:
                if e == 'X':
                    s[i] += 10
                else:
                    s[i] += int(e)
        elif len(plus) == 3:
            plus = plus[0:2]
            for o in range(len(plus)):
                if plus[o] == 'X':
                    s[i] += 10
                elif plus[o] == '/':
                    s[i] -= int(plus[o-1])
                    s[i] += 10
                else:
                    s[i] += int(plus[o])          
        elif plus[1]=='/':
            s[i] += 10
        else:
            for e in plus:
                s[i] += int(e)
    elif p[i][1] =='/':
        s[i] += 10
        plus = p[i+1][0]
        if plus=='X':
            s[i] += 10
        else:
            s[i] += int(plus)
    else:
        for e in p[i]:
            s[i] += int(e)
for i in range(len(p[9])):
    if p[9][i] == 'X':
        s[9]+=10
    elif p[9][i] == '/':
        s[9] -= int(p[9][i-1])
        s[9] += 10
    else:
        s[9] += int(p[9][i])
if 1<=n <=10:
    print(s[int(n)-1])
else:
    print(sum(s))    