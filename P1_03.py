m = int(input())
dic = {'S':['P','R'],'P':['R','S'],'R':['S','P']}
a = 0
b = 0
j = 1
t = False
while a!= m and b!=m:
    x,y = input().split()
    if x != y :
        i = dic[x].index(y)
        if i==0:
            a+=1
        else: b+= 1
    if j==3*m:
        t = True
        break
    j += 1
print(a,b)
if t:
    print('Tie')
elif a>b:
    print('Player 1 wins')
elif b>a:
    print('Player 2 wins')