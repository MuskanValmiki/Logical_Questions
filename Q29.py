list1 = []
list2 = [2]
list3 = []
if len(list1) == 0 and len(list2) == 0:
    print(0)
elif len(list1) ==0 and len(list2)!=0:
    i=0
    while i < len(list2):
        list3.append(list2[i])
        i+=1
elif len(list1)!=0 and len(list2)==0:
    i=0
    while i < len(list1):
        list3.append(list1[i])
        i+=1
else:
    i=0
    while(i<len(list1)):
        list3.append(list1[i])
        i+=1   
    j=0
    while j<len(list2):
        list3.append(list2[j])
        j+=1

# merge two list

index = 0
while index < len(list3):
    j = 0
    while j < len(list3):
        if list3[index] < list3[j]:
            list3[index],list3[j] = list3[j],list3[index]
        j += 1
    index += 1

# sort the list
k = 0
result = 0
while k < len(list3):
    if len(list3)%2==0:
        m = len(list3)//2
        temp = list3[m] + list3[m-1]
        result = temp/2
    else:
        n = len(list3)//2
        result = list3[n]
    k += 1
print(result)

# find the midium of this list
