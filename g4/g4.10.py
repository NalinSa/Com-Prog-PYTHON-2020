a = float(input())
x = a
l = 0
u = 1
while x//10 != 0:
    u += 1
    x = x//10
y = (l+u)/2
while abs(a-10**y)>(1e-10)*max(a,10**y):
    if 10**y > a:
        u = y
    else:
        l = y
    y = (l+u)/2
print(round(y,6))
  
