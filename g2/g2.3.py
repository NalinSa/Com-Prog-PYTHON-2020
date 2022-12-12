inp = input() #12/1/2019
x = inp.split("/") #['12', '1', '2019']
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
m = int(x[1])
y = int(x[2])
print(month[m-1], x[0] + ",", y)