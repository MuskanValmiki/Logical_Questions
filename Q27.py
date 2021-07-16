str = input("enter any sentence=")
new_str = str.title()
print(new_str)

# by using this title function we capital first letter

str = input("enter any sentence=")
list = str.split()
str1 = " "
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        if j == 0:
            str1 += list[i][j].upper()
        else:
            str1 += list[i][j]
        j += 1
    str1 += " "
    i += 1
print(str1)

# by using loop we want to capital first letter
