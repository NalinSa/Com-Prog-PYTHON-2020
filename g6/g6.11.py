x = input().split()
su = int(x[0],2)+int(x[1],2)
bi = bin(su)
print(bi[2::])