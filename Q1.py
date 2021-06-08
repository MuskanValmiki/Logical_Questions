user=int(input())
i=1
list=[]
while i<=user:
    num=int(input())
    list.append(num)
    i+=1
print(list)
max=0
j=0
while j<len(list):
    if list[j]>max:
        max=list[j]
    j+=1
print(max)
k=0
c=0
while k<len(list):
    if max==list[k]:
        c+=1
    k+=1
print(c)


