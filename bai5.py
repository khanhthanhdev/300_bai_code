xA, yA = map(float, input("A(xA, yA)? ").split())
xB, yB = map(float, input("B(xB, yB)? ").split())
xC, yC = map(float, input("C(xC, yC)? ").split())
xM, yM = map(float, input("M(xM, yM)? ").split())

def area(xA, yA,xB,yB,xC,yC):
    return 0.5 *abs( xA * yB - xB * yA + xB * yC - xC * yB + xC * yA - xA * yC )

d = area(xM, yM, xA, yA, xB, yB) + area(xM, yM, xA,yA,xC,yC) + area(xM, yM, xB,yB,xC,yC) - area(xA, yA, xB,yA,xC,yC)

if d > 0:
    print("M nam ngoai tam giac ABC")
elif d == 0:
    print("M nam tren canh tam giac ABC")
else:
    print("M nam trong tam giac ABC")