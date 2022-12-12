class piggybank:
 def __init__(self):
 # มีตัวแปร 4 ตัวเก็บจ านวนเหรียญของเหรียญแต่ละแบบ
    self.none = 0
    self.ntwo = 0
    self.nfive = 0
    self.nten = 0
 def add1(self, n):
 # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญบาท
    self.none += n
 def add2(self, n):
 # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสองบาท
    self.ntwo += n
 def add5(self, n):
 # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญห้าบาท
    self.nfive += n
 def add10(self, n):
    self.nten += n # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสิบบาท
 def __int__(self):
     a = self.none*1
     b = self.ntwo*2
     c = self.nfive*5
     d = self.nten*10
     return a+b+c+d
 # คืนมูลค่ารวม = ค่าของเหรียญคูณกับจ านวนเหรียญ
 def __lt__(self, rhs):
    return int(self)<int(rhs)
 # เปรียบเทียบจ านวนเงินใน self กับจ านวนเงินใน rhs
 def __str__(self):
     return '{'+'1:'+str(self.none)+', 2:'+str(self.ntwo)+', 5:'+str(self.nfive)+', 10:'+str(self.nten)+'}'
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
