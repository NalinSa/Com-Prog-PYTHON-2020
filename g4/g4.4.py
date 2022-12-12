x = input()
c = ''
for e in x:
    if e == '(':
        e = '['
    elif e == '[':
        e = '('
    elif e == ')':
        e = ']'
    elif e == ']':
        e = ')'
    c += e
print(c)
  