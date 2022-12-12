class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        if self.a==0and self.b==0:
            return '0'
        elif self.b == -1:
            return str(self.a)*(self.a!=0)+'-i'
        elif self.b == 1:
            return str(self.a)*(self.a!=0)+'+'*(self.a!=0)+'i'
        elif self.b>0:
            if self.a == 0:
                return str(self.b)+'i'
            else: return str(self.a)+'+'+str(self.b)+'i'
        return str(self.a)*(self.a!=0)+(str(self.b)+'i')*(self.b!=0) 
    def __add__(self, rhs):
        a = self.a+rhs.a
        b = self.b+rhs.b
        return Complex(a,b)
    def __mul__(self, rhs):
        a = self.a*rhs.a-self.b*rhs.b
        b = self.a*rhs.b+self.b*rhs.a
        return Complex(a,b)
    def __truediv__(self, rhs):
        a1 = self.a*rhs.a+self.b*rhs.b
        a2 = rhs.a**2+rhs.b**2
        b1 = -self.a*rhs.b+self.b*rhs.a
        return Complex(a1/a2,b1/a2)
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)
