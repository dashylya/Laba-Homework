print("-------------------------------------------------------------------")
print("первый пр€моугольник")
print("-------------------------------------------------------------------")
X1 = int( input("¬ведите координату X1 "))
X2 = int( input("¬ведите координату X2 "))  
Y1 = int( input("¬ведите координату Y1 "))  
Y2 = int( input("¬ведите координату Y2 "))   
coordXn = [0,0]         #дл€ успешного выполнени€ необходимо изначально                     
coordYl = [0,0]         #задавать меньшую координату, а после большую
coordXn[0] = X1
coordXn[1] = X2
coordYl[0] = Y1
coordYl[1] = Y2
print(coordXn)
print(coordYl)
rX = X2 - X1
rXm = rX
rY = Y2 - Y1
rYm = rY
rYt = rY
X = X1
while rX > 1:
    X = X + 1
    coordXn.insert(-1, X)
    rX = rX - 1
print(coordXn)
Y = Y1
while rY > 1:
    Y = Y + 1
    coordYl.insert(-1, Y)
    rY = rY - 1
print(coordYl)
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
rectangle = []




print("-------------------------------------------------------------------")
print("второй пр€моугольник")
print("-------------------------------------------------------------------")
XS1 = int( input("¬ведите координату XS1 "))
XS2 = int( input("¬ведите координату XS2 "))  
YS1 = int( input("¬ведите координату YS1 "))   
YS2 = int( input("¬ведите координату YS2 "))  
coordXSn = [0,0]                             
coordYSl = [0,0]
coordXSn[0] = XS1
coordXSn[1] = XS2
coordYSl[0] = YS1
coordYSl[1] = YS2
print(coordXSn)
print(coordYSl)
rXS = XS2 - XS1
rYS = YS2 - YS1
XS = XS1
while rXS > 1:
    XS = XS + 1
    coordXSn.insert(-1, XS)
    rXS = rXS - 1
print(coordXSn)
YS = YS1
while rYS > 1:
    YS = YS + 1
    coordYSl.insert(-1, YS)
    rYS = rYS - 1
print(coordYSl)
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")

