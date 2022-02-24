# def toa_do(x1,x2,y1,y2):
#     return ((y1-x1)**2+(y2-x2)**2)**0.5

# x1 = float(input("x1: "))
# x2 = float(input("x2: "))
# y1 = float(input("y1: "))
# y2 = float(input("y2: "))
# print(toa_do(x1,x2,y1,y2))

xA, yA = map(float, input().split())
xB, yB = map(float, input().split())

print(  ((xB - xA)**2 + (yB - yA)**2) ** 0.5)