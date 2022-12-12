real = ['Robert', 'William', 'James', 'John', 'Margaret','Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
n = int(input())
k = 0
while k < n:
    x = input()
    if x in real:
        y = real.index(x)
        print(nick[y])
    elif x in nick:
        y = nick.index(x)
        print(real[y])
    else:
        print('Not found')
    k += 1