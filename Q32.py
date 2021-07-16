m=0
row=1
while row<=5:
    m = m+row
    column=m
    while column>m-row:
        print(column,end="")
        column-=1
    print()
    row+=1