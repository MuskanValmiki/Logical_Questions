a=[[3,16,2,5],[7,3,8,2]]
list1=a[0]
list2=a[1]
i=0
sum=0
multi=1
while i<len(list1):
    if list1 in a:
        multi=multi*list1[i]
    if list2 in a:
        sum=sum+list2[i]
    i+=1
print(sum)
print(multi)
