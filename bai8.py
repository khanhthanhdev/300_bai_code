import math
a,b,c = map(float, input("Nhap a, b, c: ").split())

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        print("x1 = {}".format(x1))
        print("x2 = {}".format(x2))
    elif delta == 0:
        x = (-b) / (2*a)
        print("x1 = x2 = {}".format(x))
    elif delta < 0:
        print("Vo nghiem")