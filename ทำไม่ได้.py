def spiral_square(n): # n is a positive odd number
    l = []
    s = []
    for i in range(1,n+1,2):
        l.append(list(range(i**2-i+1,i**2+1,)))
        s += list(range(i**2-i+1,i**2+1,))
        j=i**2-4*(int(i/2))+1
        if i >1:
            l.insert(0,list(range(j-i,j,))[::-1])
            s += list(range(j-i,j,))[::-1]
        for j in range(2,i**2+1,):
            if j not in s:
                s += j
                
            
    return l
        

def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
 for i in range(len(S)):
     print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
print(spiral_square(3))