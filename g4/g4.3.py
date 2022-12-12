a = input()
b = input()
c = 0
if len(a) != len(b):
  print('Incomplete answer')
else:
  for i in range(len(a)):
    if a[i]==b[i]:
      c += 1
  print(c)