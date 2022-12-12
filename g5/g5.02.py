x = input()
if x == 'str2RLE':
    y = input() 
    i = 0
    s = ''
    while i < len(y):
        c = 1
        alphabet = y[i]
        j = i
        while j < len(y)-1:
            if y[j] == y[j+1]:
                c += 1
            else:
                break
            j += 1
        i = j + 1
        s = s+alphabet+' '+str(c)+' '
    print(s)
elif x == 'RLE2str':
    y = input().split()
    z = ''
    for i in range(0,len(y)-1,2):
        z += y[i]*int(y[i+1])
    print(z)
else:
    print('Error')
    