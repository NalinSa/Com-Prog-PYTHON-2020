# Prog-04: Mastermind Game 
# 6330271121 Nalin Baipluthong

import random
import math

WINNING_MSG = "Congratulations! You won the game."
LOSING_MSG = "Sorry! You just lost it."

code = ''.join(random.sample('ABCDEF', 4))

print('Please guess the puzzle code using')
print('the four distinct code characters from [A to F]:')

#---------------------------------------------------
def cal(t):
    p = 0
    v = 0
    x = 0
    if t[0] == code[0] and t[1]==code[1] and t[2]==code[2] and t[3] != code [3]:
        p+= 3
        x += 1
    if t[0] == code[0] and t[1]==code[1] and t[2]!=code[2] and t[3] == code [3]:
        p+= 3
        x += 1
    if t[0] == code[0] and t[1]!=code[1] and t[2]==code[2] and t[3] == code [3]:
        p+=3
        x += 1
    if t[0] != code[0] and t[1]==code[1] and t[2]==code[2] and t[3] == code [3]:
        p+=3
        x+=1
    if t[0] != code[0] and t[1]!=code[1] and t[2]==code[2] and t[3] == code [3]:
        p += 2
        if t[1] == code[0]:
            v += 1
            if t[0] == code[1]:
                v+=1
            else:
                x += 1
        else:
            x += 1
            if t[0] == code[1]:
                v+=1
            else:
                x+=1
    if t[0] != code[0] and t[1]==code[1] and t[2]!=code[2] and t[3] == code [3]:
        p += 2
        if t[2] == code[0]:
            v += 1
            if t[0] == code[2]:
                v+=1
            else:
                x += 1
        else:
            x += 1
            if t[0] == code[2]:
                v+=1
            else:
                x+=1
    if t[0] != code[0] and t[1]==code[1] and t[2]==code[2] and t[3] != code [3]:
        p += 2
        if t[3] == code[0]:
            v += 1
            if t[0] == code[3]:
                v+=1
            else:
                x += 1
        else:
            x += 1
            if t[0] == code[3]:
                v+=1
            else:
                x+=1
    if t[0] == code[0] and t[1]!=code[1] and t[2]!=code[2] and t[3] == code [3]:
        p += 2
        if t[2] == code[1]:
            v += 1
            if t[1] == code[2]:
                v+=1
            else:
                x += 1
        else:
            x += 1
            if t[1] == code[2]:
                v+=1
            else:
                x+=1
    if t[0] == code[0] and t[1]==code[1] and t[2]!=code[2] and t[3] != code [3]:
        p += 2
        if t[3] == code[2]:
            v += 1
            if t[2] == code[3]:
                v+=1
            else:
                x += 1
        else:
            x += 1
            if t[2] == code[3]:
                v+=1
            else:
                x+=1
    if t[0] == code[0] and t[1]!=code[1] and t[2]==code[2] and t[3] != code [3]:
        p += 2
        if t[3] == code[1]:
            v += 1
            if t[1] == code[3]:
                v+=1
            else:
                x += 1
        else:
            x += 1
            if t[1] == code[3]:
                v+=1
            else:
                x+=1
    if t[0] != code[0] and t[1]!=code[1] and t[2]!=code[2] and t[3] == code [3]:
        p+=1
        if t[0]==code[2] and t[1]==code[0] and t[2]==code[1]:
            v += 3
        if t[0]==code[1] and t[1]==code[2] and t[2]==code[0]:
            v += 3
        if t[0] not in code[0:3:] and t[1]==code[0] and t[2]==code[1]:
            v += 2
            x += 1
        if t[0]==code[2] and t[1] not in code[0:3:] and t[2]==code[1]:
            v += 2
            x += 1
        if t[0]==code[2] and t[1]==code[0] and t[2] not in code[0:3:]:
            v += 2
            x += 1
        if t[0] not in code[0:3:] and t[1]==code[2] and t[2]==code[0]:
            v += 2
            x += 1
        if t[0]==code[1] and t[1] not in code[0:3:] and t[2]==code[0]:
            v += 2
            x += 1
        if t[0]==code[1] and t[1]==code[2] and t[2] not in code[0:3:]:
            v += 2
            x += 1
        if t[0] not in code[0:3:] and t[1] not in code[0:3:] and t[2]==code[1]:
            v += 1
            x += 2
        if t[0] not in code[0:3:] and t[1]==code[0] and t[2] not in code[0:3:]:
            v += 1
            x += 2
        if t[0]==code[2] and t[1] not in code[0:3:] and t[2] not in code[0:3:]:
            v += 1
            x += 2
        if t[0]==code[1] and t[1] not in code[0:3:] and t[2] not in code[0:3:]:
            v += 1
            x += 2
        if t[0] not in code[0:3:] and t[1]==code[2] and t[2] not in code[0:3:]:
            v += 1
            x += 2
        if t[0] not in code[0:3:] and t[1] not in code[0:3:] and t[2]==code[0]:
            v += 1
            x += 2
        if t[0] not in code[0:3:] and t[1] not in code[0:3:] and t[2] not in code[0:3:]:
            x += 3
    if t[0] != code[0] and t[1]!=code[1] and t[2]==code[2] and t[3] != code [3]:
        p+=1
        if t[0]==code[3] and t[1]==code[0] and t[3]==code[1]:
            v += 3
        if t[0]==code[1] and t[1]==code[3] and t[3]==code[0]:
            v += 3
        if t[0] not in [code[0], code[1], code[3]] and t[1]==code[0] and t[3]==code[1]:
            v += 2
            x += 1
        if t[0]==code[3] and t[1] not in [code[0], code[1], code[3]] and t[3]==code[1]:
            v += 2
            x += 1
        if t[0]==code[3] and t[1]==code[0] and t[3] not in [code[0], code[1], code[3]]:
            v += 2
            x += 1
        if t[0] not in [code[0], code[1], code[3]] and t[1]==code[3] and t[3]==code[0]:
            v += 2
            x += 1
        if t[0]==code[1] and t[1] not in [code[0], code[1], code[3]] and t[3]==code[0]:
            v += 2
            x += 1
        if t[0]==code[1] and t[1]==code[3] and t[3] not in [code[0], code[1], code[3]]:
            v += 2
            x += 1
        if t[0] not in [code[0], code[1], code[3]] and t[1] not in [code[0], code[1], code[3]] and t[3]==code[1]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[1], code[3]] and t[1]==code[0] and t[3] not in [code[0], code[1], code[3]]:
            v += 1
            x += 2
        if t[0]==code[3] and t[1] not in [code[0], code[1], code[3]] and t[3] not in [code[0], code[1], code[3]]:
            v += 1
            x += 2
        if t[0]==code[1] and t[1] not in [code[0], code[1], code[3]] and t[3] not in [code[0], code[1], code[3]]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[1], code[3]] and t[1]==code[3] and t[3] not in [code[0], code[1], code[3]]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[1], code[3]] and t[1] not in [code[0], code[1], code[3]] and t[3]==code[0]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[1], code[3]] and t[1] not in [code[0], code[1], code[3]] and t[3] not in [code[0], code[1], code[3]]:
            x += 3
    if t[0] != code[0] and t[1]==code[1] and t[2]!=code[2] and t[3] != code [3]:
        p+=1
        if t[0]==code[3] and t[2]==code[0] and t[3]==code[2]:
            v += 3
        if t[0]==code[2] and t[2]==code[3] and t[3]==code[0]:
            v += 3
        if t[0] not in [code[0], code[2], code[3]] and t[2]==code[0] and t[3]==code[2]:
            v += 2
            x += 1
        if t[0]==code[3] and t[2] not in [code[0], code[2], code[3]] and t[3]==code[2]:
            v += 2
            x += 1
        if t[0]==code[3] and t[2]==code[0] and t[3] not in [code[0], code[2], code[3]]:
            v += 2
            x += 1
        if t[0] not in [code[0], code[2], code[3]] and t[2]==code[3] and t[3]==code[0]:
            v += 2
            x += 1
        if t[0]==code[2] and t[2] not in [code[0], code[2], code[3]] and t[3]==code[0]:
            v += 2
            x += 1
        if t[0]==code[2] and t[2]==code[3] and t[3] not in [code[0], code[2], code[3]]:
            v += 2
            x += 1
        if t[0] not in [code[0], code[2], code[3]] and t[2] not in [code[0], code[2], code[3]] and t[3]==code[2]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[2], code[3]] and t[2]==code[0] and t[3] not in [code[0], code[2], code[3]]:
            v += 1
            x += 2
        if t[0]==code[3] and t[2] not in [code[0], code[2], code[3]] and t[3] not in [code[0], code[2], code[3]]:
            v += 1
            x += 2
        if t[0]==code[2] and t[2] not in [code[0], code[2], code[3]] and t[3] not in [code[0], code[2], code[3]]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[2], code[3]] and t[2]==code[3] and t[3] not in [code[0], code[2], code[3]]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[2], code[3]] and t[2] not in [code[0], code[2], code[3]] and t[3]==code[0]:
            v += 1
            x += 2
        if t[0] not in [code[0], code[2], code[3]] and t[2] not in [code[0], code[2], code[3]] and t[3] not in [code[0], code[2], code[3]]:
            x += 3
    if t[0] == code[0] and t[1]!=code[1] and t[2]!=code[2] and t[3] != code [3]:
        p+=1
        if t[1]==code[3] and t[2]==code[1] and t[3]==code[2]:
            v += 3
        if t[1]==code[2] and t[2]==code[3] and t[3]==code[1]:
            v += 3
        if t[1] not in [code[1], code[2], code[3]] and t[2]==code[1] and t[3]==code[2]:
            v += 2
            x += 1
        if t[1]==code[3] and t[2] not in [code[1], code[2], code[3]] and t[3]==code[2]:
            v += 2
            x += 1
        if t[1]==code[3] and t[2]==code[1] and t[3] not in [code[1], code[2], code[3]]:
            v += 2
            x += 1
        if t[1] not in [code[1], code[2], code[3]] and t[2]==code[3] and t[3]==code[1]:
            v += 2
            x += 1
        if t[1]==code[2] and t[2] not in [code[1], code[2], code[3]] and t[3]==code[1]:
            v += 2
            x += 1
        if t[1]==code[2] and t[2]==code[3] and t[3] not in [code[1], code[2], code[3]]:
            v += 2
            x += 1
        if t[1] not in [code[1], code[2], code[3]] and t[2] not in [code[1], code[2], code[3]] and t[3]==code[2]:
            v += 1
            x += 2
        if t[1] not in [code[1], code[2], code[3]] and t[2]==code[1] and t[3] not in [code[1], code[2], code[3]]:
            v += 1
            x += 2
        if t[1]==code[3] and t[2] not in [code[1], code[2], code[3]] and t[3] not in [code[1], code[2], code[3]]:
            v += 1
            x += 2
        if t[1]==code[2] and t[2] not in [code[1], code[2], code[3]] and t[3] not in [code[1], code[2], code[3]]:
            v += 1
            x += 2
        if t[1] not in [code[1], code[2], code[3]] and t[2]==code[3] and t[3] not in [code[1], code[2], code[3]]:
            v += 1
            x += 2
        if t[1] not in [code[1], code[2], code[3]] and t[2] not in [code[1], code[2], code[3]] and t[3]==code[1]:
            v += 1
            x += 2
        if t[1] not in [code[1], code[2], code[3]] and t[2] not in [code[1], code[2], code[3]] and t[3] not in [code[1], code[2], code[3]]:
            x += 3
    if t[0] != code[0] and t[1]!=code[1] and t[2]!=code[2] and t[3] != code [3]:
        x += 4
        if t[0] in code:
            v += 1
            x -= 1
        if t[1] in code:
            v += 1
            x -= 1
        if t[2] in code:
            v += 1
            x -= 1
        if t[3] in code:
            v += 1
            x -= 1
    result = [p,v,x]
    return result

t = input('Turn #1 : ')
if t[0] == code[0] and t[1]==code[1] and t[2]==code[2] and t[3] == code [3]:
    print(WINNING_MSG)
else :
    p,v,x = cal(t)
    print('          P='+str(p)+',V='+str(v)+',X='+str(x))
    t = input('Turn #2 : ')
    if t[0] == code[0] and t[1]==code[1] and t[2]==code[2] and t[3] == code [3]:
        print(WINNING_MSG)
    else :
        p,v,x = cal(t)
        print('          P='+str(p)+',V='+str(v)+',X='+str(x))
        t = input('Turn #3 : ')
        if t[0] == code[0] and t[1]==code[1] and t[2]==code[2] and t[3] == code [3]:
            print(WINNING_MSG)
        else :
            p,v,x = cal(t)
            print('          P='+str(p)+',V='+str(v)+',X='+str(x))
            t = input('Turn #4 : ')
            if t[0] == code[0] and t[1]==code[1] and t[2]==code[2] and t[3] == code [3]:
                print(WINNING_MSG)
            else :
                p,v,x = cal(t)
                print('          P='+str(p)+',V='+str(v)+',X='+str(x))
                print(LOSING_MSG)
                print('The answer is',code)
                print('Please try again...')