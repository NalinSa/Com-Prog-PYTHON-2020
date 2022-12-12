def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    i = N+1
    while i > N:
        if is_prime(i):
            return i
            break
        else: i += 1       
def next_twin_prime(N):
    i = N+1
    while i > N:
        if is_prime(i) and is_prime(i+2):
            return (i, i+2)
            break
        else: i += 1

print(next_twin_prime(198))