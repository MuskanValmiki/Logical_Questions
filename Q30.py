list = [{"name":"Muskan","age":18,"subject":"science"},{"name":"Kajal","age":23,"subject":"maths"},{"name":"Aditya","age":21,"subject":"commerse"},{"name":"Kashish","age":16,"subject":"physics"}]
i = 0
user = input("enter any name =")
while i < len(list):
    for key in list[i]:
        if list[i][key] == user:
            print(list[i])
    i += 1
