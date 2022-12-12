x = input() 
i = 0
s = ''
while i < len(x):
    c = 1
    alphabet = x[i]
    j = i
    while j < len(x)-1:
        if x[j] == x[j+1]:
            c += 1
        else:
            break
        j += 1
    i = j + 1
    s = s+alphabet+' '+str(c)+' '
print(s)