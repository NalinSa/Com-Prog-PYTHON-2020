x = input()
c = 0
y = 0
if x == 'q':
  print('No Data')
else :
    while x != 'q':
        c += float(x)
        x = input()
        y += 1
    print(round(c/y,2))