dict1={"a":29,"b":55,"c":90,"d":177,"e":123,"f":76}
max=0
sec=0
third=0
for key in dict1:
    if dict1[key]>max:
        max=dict1[key]
for key1 in dict1:
    if max>dict1[key1]>sec:
        sec=dict1[key1]
for key2 in dict1:
    if max>sec>dict1[key2]>third:
        third=dict1[key2]
print(max)
print(sec)
print(third)
