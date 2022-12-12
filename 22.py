l1 = [int(e) for e in input().split()]
l2 = [int(e) for e in input().split()]
l3 = [int(e) for e in input().split()]
l4 = [int(e) for e in input().split()]
l5 = [int(e) for e in input().split()]
l6 = [int(e) for e in input().split()]
l7 = [int(e) for e in input().split()]
l8 = [int(e) for e in input().split()]
l9 = [int(e) for e in input().split()]
l = [l1,l2,l3,l4,l5,l6,l7,l8,l9]
par = []
stroke = []
stpp = []
for e in l:
    par.append(e[0])
    stroke.append(e[1])
    stpp.append(min([e[1],e[0]+2])*e[2])
print(sum(stroke))
tt = int((0.8*(1.5*sum(stpp)-sum(par)))//1)
print(tt)
print(sum(stroke)-tt)
    
    
