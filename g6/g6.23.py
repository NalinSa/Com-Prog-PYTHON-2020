def make_int_list(x):
    y = x.split()
    return y
def is_odd(e):
    if e%2 != 0 :
        return True
    else: return False
def odd_list(alist):
    c = []
    for e in alist:
        if is_odd(e):
            c.append(e)
    return c
def sum_square(alist):
    c = 0
    for e in alist:
        c += e**2
    return c
print(make_int_list('10 23 32 11 99 9999 2 0 -2'))