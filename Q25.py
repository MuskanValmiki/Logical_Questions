str = input("enter any sentence=")
sum_digit  =  0
for i in range(0,len(str)):
    if (str[i].isdigit()):
        sum_digit += int(str[i])
print(sum_digit)

# here we collect sum of digit