x = int(input())
print(' '*(x-1)+'*')
for i in range(2,x,1):
  print(' '*(x-i)+'*'+' '*(2*i-3)+'*')
print('*'*(x*2-1))