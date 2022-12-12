x = input().strip()
n = int(input().strip())
word = input().strip()
lenn = len(word)
t = False
for i in range(n-1):
    y = input().strip()
    if len(y) != lenn:
        t = True
    word += y
if t:
    print('Invalid size')
else:
    if x == '90':
        for i in range(lenn):
            print(word[i::lenn][::-1])
    if x == 'flip':
        for i in range(n):
            print(word[lenn*i:lenn*i+lenn:][::-1])
    if x == '180':
        for i in range(-1,-n-1,-1):
            print(word[-1-lenn*(-i-1):-1-lenn*(-i-1)-lenn:-1])