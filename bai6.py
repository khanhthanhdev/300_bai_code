a,b,c = map(int, input("Nhap a,b,c: ").split())

# sort a b c then print out
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print("Tăng dần: {0} {1} {2}".format(a,b,c))