# Prog-05: The 24 Game
# 6330271121 Nalin Baipluthong

from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                       product(operators, repeat=3)): 
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#--------------------------------------------------------- 
def cal(num1, op, num2):
    if op == '+':
        r = num1 + num2
    elif op == '-':
        r = num1 - num2
    elif op == '*':
        r = num1*num2
    elif op == '/':
        if num2 != 0:
            r = num1/num2
        else:
            r = 1.234**9.17
    return r    
#---------------------------------------------------------
nums = [int(e) for e in input('Enter 4 integers: ').split()]
cases = generate_all_combinations( nums,  '+-*/' )
C = cases
c = 0
for i in range(len(C)):
    a = C[i]
    if cal(cal(cal(a[0], a[1], a[2]), a[3], a[4]), a[5], a[6]) == 24 :
        c = 1
        print('(','(',a[0],a[1],a[2],')',a[3],a[4],')',a[5],a[6],'= 24')
        break
    if cal(cal(a[0], a[1], cal(a[2],a[3],a[4])),a[5],a[6]) == 24:
        c = 1
        print('(',a[0],a[1],'(',a[2],a[3],a[4],')',')',a[5],a[6],'= 24')
        break
    if cal(cal(a[0],a[1],a[2]),a[3], cal(a[4],a[5],a[6])) == 24:
        c = 1
        print('(',a[0],a[1],a[2],')',a[3],'(',a[4],a[5],a[6],')','= 24')
        break
    if cal(a[0],a[1],cal(cal(a[2],a[3],a[4]),a[5],a[6])) == 24:
        c = 1
        print(a[0],a[1],'(','(',a[2],a[3],a[4],')',a[5],a[6],')','= 24')
        break
    if cal(a[0],a[1],cal(a[2],a[3],cal(a[4],a[5],a[6]))) == 24:
        c = 1
        print(a[0],a[1],'(',a[2],a[3],'(',a[4],a[5],a[6],')',')','= 24')
        break
if c == 0:
    print('No Solutions')