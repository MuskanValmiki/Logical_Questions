list=[1,2,3,4,5,6,7,8,9,10]
user=int(input())
i=-1
while i>=(-len(list)):
    if user not in list:
        print("NIL")
        break
    elif user==i*(-1):
        print(list[i])
        break
    i-=1
    