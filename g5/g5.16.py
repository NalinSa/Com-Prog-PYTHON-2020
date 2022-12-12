n = int(input())
c = []
c.append(str(n))
while n != 1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    c.append(str(n))
print('->'.join(c[-15::1]))