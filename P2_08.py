read = ['soon','neung','song','sam','si','ha','hok','chet','paet','kao','sip','et','yi','roi','pun']
num = [0,1,2,3,4,5,6,7,8,9]
def to_Thai( N ):
    word = ''
    t = False
    if N >1:
        t = True
    if N//1000>0:
        i = num.index(N//1000)
        word += ' ' + read[i] + ' pun'
        N = N%1000
    if N//100>0:
        i = num.index(N//100)
        word += ' '+read[i] + ' roi'
        N = N%100        
    if N//10>0:
        if str(N)[0]=='2':
            word += ' '+'yi'
            N = N%20
        elif N//10==1:
            N = N%10
            pass
        else:
            i = num.index(N//10)
            word += ' '+ read[i] 
            N = N%10
        word += ' '+'sip'
    if t:
        if N==1:
            word += ' '+'et'
        elif N>1:
            i = num.index(N)
            word += ' '+read[i]       
    else:
        if N==1:
            word += ' '+'neung'
        else:
            word += ' '+'soon'
    return word.strip()
for k in range(11,300,10): print(to_Thai(k))