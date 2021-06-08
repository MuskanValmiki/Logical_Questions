a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if len(a)>len(a[i]):
            temp=len(a[i]),a[i]
        j+=1
    i+=1
print(temp)
