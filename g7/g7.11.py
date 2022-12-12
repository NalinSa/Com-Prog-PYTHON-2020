x = input()
if x[-1] in ['s','x']:
    x += 'es'
elif x[-2::1] == 'ch':
    x += 'es'
elif x[-1] == 'y':
    if x[-2] not in 'aeiou':
        x = x[:-1:1]+'ies'
    else: x += 's'
else: x += 's'
print(x)