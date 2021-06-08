l=[[4,2],[2,5],[3,7],[1,3],[4,0]]
i=0
max=0
min=l[i][0]
while i<len(l):
    if l[i][1]>max:
        max=l[i][1]
    if l[i][0]<min:
        min=l[i][0]
    i+=1
print(max)
print(min)



