n = int(input())
k = int(input())
if n<=0 and k<1:
    print('Invalid n and k')
elif n<=0:
    print('Invalid n')
elif k<1:
    print('Invalid k')
else:
    out = ''
    for i in range(1,k+1):
            if i <= k-1:
                m = n+1
            else:
                m = n        
            out += str(i) + '-'*(m-len(str(i)))
    print(out)
    bit1 = ['0','1']
    for i in range(n-1):
        bit2 = bit1[::-1]
        for j in range(len(bit1)):
            bit1[j] = '0'+bit1[j]
            bit2[j] = '1'+bit2[j]
        bit1 += bit2
    for u in range(0,len(bit1),k):
        print(','.join(bit1[u:u+k]))
            
        