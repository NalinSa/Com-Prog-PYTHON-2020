def distance1(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    return d
def distance2(p1,p2):
    d = ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    return d
def distance3(c1,c2):
    d = ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5
    if d<=(c1[2]+c2[2]):
        k = True
    else :
        k = False
    return d,k
def perimeter(points):
    d = 0
    for i in range(len(points)):
        d += abs(points[i][0]-points[i-1][0])+abs(points[i][1]-points[i-1][1])
    return d
print(distance1(0, 0, 3, 4))