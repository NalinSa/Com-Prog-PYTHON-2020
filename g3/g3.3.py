x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
d = float(x[3])
if a>=b>=c>=d or a>=c>=b>=d or d>=b>=c>=a or d>=c>=b>=a:
    y = (b+c)/2
elif d>=a>=b>=c or d>=b>=a>=c or c>=a>=b>=d or c>=b>=a>=d:
    y = (a+b)/2
elif c>=d>=a>=b or c>=a>=d>=b or b>=d>=a>=c or b>=a>=d>=c:
    y = (d+a)/2
elif b>=c>=d>=a or b>=d>=c>=a or a>=c>=d>=b or a>=d>=c>=b:
    y = (c+d)/2
print(round(y,2))