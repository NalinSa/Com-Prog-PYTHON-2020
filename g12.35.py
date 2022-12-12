class roman :
    def __init__(self, r):
        if '0'<=str(r)[0] <= '9':
            self.r = r
            return
        n = 0
        l = r
        l1 = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        l2 =[1, 5, 10, 50, 100, 500, 1000]
        if 'IV' in l:
            n += 4
            j = l.find('IV')
            l = l[0:j]+l[j+2:]
        if 'IX' in l:
            n += 9
            j = l.find('IX')
            l = l[0:j]+l[j+2:]
        if 'XL' in l:
            n += 40
            j = l.find('XL')
            l = l[0:j]+l[j+2:]
        if 'XC' in l:
            n += 90
            j = l.find('XC')
            l = l[0:j]+l[j+2:]
        if 'CD' in l:
            n += 400
            j = l.find('CD')
            l = l[0:j]+l[j+2:]
        if 'CM' in l:
            n += 900
            j = l.find('CM')
            l = l[0:j]+l[j+2:]
        for e in l:
            j = l1.index(e)
            n += l2[j]
        self.r = n
 
    
    def __lt__(self, rhs):
        return self.r<rhs.r
    
    def __str__(self):
        n = self.r
        l = ''
        while n>=1000:
            l += 'M'
            n  -= 1000
        while n>= 900:
            l += 'CM'
            n -= 900
        while n>= 500:
            l += 'D'
            n -= 500
        while n>= 400:
            l += 'CD'
            n -= 400
        while n>= 100:
            l += 'C'
            n -= 100
        while n>= 90:
            l += 'XC'
            n -= 90
        while n>= 50:
            l += 'L'
            n -= 50
        while n>= 40:
            l += 'XL'
            n -= 40
        while n>= 10:
            l += 'X'
            n -= 10
        while n>= 9:
            l += 'IX'
            n -= 9
        while n>= 5:
            l += 'V'
            n -= 5
        while n>= 4:
            l += 'IV'
            n -= 4
        while n>= 1:
            l += 'I'
            n -= 1
        return l    
    def __int__(self):
        return int(self.r)
    def __add__(self, rhs):
        return roman(self.r+rhs.r)  
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))