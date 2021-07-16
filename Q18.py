list = [["a","b"],["c","d"]]
print(list[0][0],list[1][0])
print(list[0][0],list[1][1])
print(list[0][1],list[1][0])
print(list[0][1],list[1][1])

# ac,ad,bc,bd 

i = 0
while i<len(list):
    j=0
    while j<len(list[i]):
        print(list[i],list[j])
        j+=1
    i+=1
# half
