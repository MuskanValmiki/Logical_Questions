
x=int(input("enter a number="))
y=int(input("enter a number="))
z=int(input("enter a number="))
d1 = x-z
d2 = y-z
if d1 == d2:
    print('Mouse C')
elif d1 < d2:
    print('Cat A')
elif d1 > d2:
    print('Cat B')