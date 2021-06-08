i=0
while i<=100:
    j=2
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==1:
        print(i,"prime")
    i+=1
