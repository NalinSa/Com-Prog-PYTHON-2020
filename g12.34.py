class piggybank:
 def __init__(self):
    self.coins = {} # มีตัวแปร self.coins เก็บ dict เริ่มต้นให้ว่าง ๆ
 # มี key เป็นมูลค่าเหรียญ และ value เป็นจ านวนเหรียญ
 def add(self, v, n):
    nn = sum(self.coins.values())
    if nn+n<=100:
        if float(v) in self.coins:
            self.coins[float(v)] += n
        else:
            self.coins[float(v)] = n
        return True
    else: return False# ถ้าเพิ่มจ านวนเหรียญในกระปุกอีก n เหรียญแล้วเกิน 100
 # จะไม่ให้เพิ่ม ให้คืน False แทนว่า เพิ่มไม่ส าเร็จ
 # แปลง v เป็น float ก่อน (เพิ่ม 5 กับ 5.0 จะได้เหมือนกัน)
 # ถ้ากระปุกไม่เคยมีเหรียญ v ท า self.coins[v]= 0
 # ท าค าสั่ง self.coins[v] += n
 # คืน True แทนว่าเพิ่มส าเร็จ
 def __float__(self):
     n = 0.0
     for key in self.coins:
         n += key*self.coins[key]
     return n
    
 def __int__(self):
     n = 0
     for key in self.coins:
         n += key*self.coins[key]
     return int(n)
 # น าค่าของเหรียญคูณกับจ านวนเหรียญ ของเหรียญทุกแบบ
 # ต้องคืนจ านวนแบบ float เท่านั้น อยากคืนศูนย์ ก็ต้อง 0.0
 def __str__(self):
    a = [str(key)+':'+str(self.coins[key]) for key in sorted(self.coins)]
    return '{'+', '.join(a)+'}'
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)