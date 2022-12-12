x1 = input().split(',')
y1 = ' '.join(x1)
z1 = y1.split()
z1 = [int(z1[-1]),z1[1],int(z1[2]),z1[0]]
x2 = input().split(',')
y2 = ' '.join(x2)
z2 = y2.split()
z2 = [int(z2[-1]),z2[1],int(z2[2]),z2[0]]
month =['January','February','March','April','May','June','July','August','September','October','November','December']
if z1[1] in month:
    z1[1] = month.index(z1[1])
if z2[1] in month:
    z2[1] = month.index(z2[1])
if z1[:3:] == z2[:3:]:
    print(z1[3],z2[3])
elif z1[:3:]>z2[:3:]:
    print(z2[3])
elif z1[:3:]<z2[:3:]:
    print(z1[3])