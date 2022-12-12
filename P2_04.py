x = input().split()
def date(m,y):
  if m == 2:
    yc = y-543
    if (yc%400==0) or (yc%4==0 and yc%100 != 0):
      return 29
    else: return 28
  else:
    if m in [1,3,5,7,8,10,12]:
      return 31
    elif m in [4,6,9,11]:
      return 30
lis = []      
while x[0] != 'END':
  if int(x[4])<2558:
    print('Error:', ' '.join(x), '-->', 'Invalid year')
  elif not(1<=int(x[3])<=12):
    print('Error:', ' '.join(x), '-->', 'Invalid month')
  elif not(1<=int(x[2])<=date(int(x[3]),int(x[4]))):
    print('Error:', ' '.join(x), '-->', 'Invalid date')
  elif x[1] not in ['E','Q','N','F']:
    print('Error:',' '.join(x),'-->','Invalid delivery type')
  else:
    d = date(int(x[3]),int(x[4]))
    if x[1]=='E':
      if int(x[2])+1>d:
        if int(x[3])+1 > 12:
          lis.append([str(int(x[4])+1),'1','1',x[0]])
        else:
          lis.append([x[4],str(int(x[3])+1),'1',x[0]])
      else:
        lis.append([x[4],x[3],str(int(x[2])+1),x[0]])
    if x[1] == 'Q':
      if int(x[2])+3>d:
        if int(x[3])+1 > 12:
          lis.append([str(int(x[4])+1),'1',str(int(x[2])+3-d),x[0]])
        else:
          lis.append([x[4],str(int(x[3])+1),str(int(x[2])+3-d),x[0]])
      else:
        lis.append([x[4],x[3],str(int(x[2])+3),x[0]])     
    if x[1] == 'N':
      if int(x[2])+7>d:
        if int(x[3])+1 > 12:
          lis.append([str(int(x[4])+1),'1',str(int(x[2])+7-d),x[0]])
        else:
          lis.append([x[4],str(int(x[3])+1),str(int(x[2])+7-d),x[0]])
      else:
        lis.append([x[4],x[3],str(int(x[2])+7),x[0]]) 
    if x[1] == 'F':
      if int(x[2])+14>d:
        if int(x[3])+1 > 12:
          lis.append([str(int(x[4])+1),'1',str(int(x[2])+14-d),x[0]])
        else:
          lis.append([x[4],str(int(x[3])+1),str(int(x[2])+14-d),x[0]])
      else:
        lis.append([x[4],x[3],str(int(x[2])+14),x[0]])
  x = input().split()
l = []
for y,m,d,n in lis:
    l.append([int(y),int(m),int(d),n])
l.sort()
for y,m,d,n in l:
    print(n+': delivered on '+str(d)+'/'+str(m)+'/'+str(y))