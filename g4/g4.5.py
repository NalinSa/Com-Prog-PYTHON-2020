a = input()
x = input()
y = ''
for i in range(len(x)):
    if x[i] in ['"','(',')',',','.',"'"]:
        z = ' '
    else:
        z = x[i]
    y += z
b = y.split()
print(b)
c = 0
for i in range(len(b)):
  if a == b[i]:
    c += 1
print(c)