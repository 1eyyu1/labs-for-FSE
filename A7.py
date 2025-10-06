print("Ввод:")

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

z1 = (x1 + y1) % 2
z2 = (x2 + y2) % 2

if z1 == z2:
    print("Yes")
    if z1 == 0:
        print("White")
    else:
        print("Black")
else:
    print("No")