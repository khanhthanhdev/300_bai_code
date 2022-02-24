a,b,c = map(float, input("Nhap 3 canh tam giac: ").split())
p = (a+b+c)/2
# check right triangle

if a+b > c or a+c > b or b+c > a:
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    if a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
        print("Tam giac vuong")
        print("Dien tich tam giac la: ", S)
    elif a==b==c:
        print("Tam giac deu")
        print("Dien tich tam giac la: ", S)
    elif a==b or b==c or a==c:
        print("Tam giac can")
        print("Dien tich tam giac la: ", S)
    else:
        print("Tam giac thuong")
        print("Dien tich tam giac la: ", S)
