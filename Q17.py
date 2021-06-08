a=[40,23,70,56,12,50,5,10]
i=0
max=0
sec=0
third=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    if max>a[i]>sec:
        sec=a[i]
    if max>sec>a[i]>third:
        third=a[i]
    i+=1
print(max)
print(sec)
print(third)

# third max in list
