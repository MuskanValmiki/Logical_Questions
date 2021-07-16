string = input("enter any sentence=")
i = 0
upper_count = 0
lower_count = 0
while i < len(string):
    if (string[i].isupper()):
        upper_count += 1
    elif (string[i].islower()):
        lower_count += 1
    i += 1
print("uppercase ",upper_count)
print("lowercase ",lower_count)

# count how many letter upper or lower
