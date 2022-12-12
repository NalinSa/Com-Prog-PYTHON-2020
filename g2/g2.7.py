a = input()
b = a[3::7]
c = a[7::5]
d = str(int(b)+int(c)+10000)
e = d[-4:-1:1]
f = ((int(e[0])+int(e[1])+int(e[2]))%10)+1
g = ['','A','B','C','D','E','F','G','H','I','J']
print(e+g[f])