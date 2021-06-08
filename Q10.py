n1=input("enter any number=")
n2=input("enter any number=")
if n1!="" and n2!="":
    print(int(n1)+int(n2))
    print(type(n1))
    print(type(n2))
elif n1!="" and n2=="":
    print(int(n1))
    print(type(n1))
    print(type(n2))
elif n1=="" and n2=="":
    print(0)
    print(type(n1))
    print(type(n2))