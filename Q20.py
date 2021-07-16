str1 = "Welcome \tto my Blog"
str2 = "Welcome to\n my \tBlog"
print(str1)                
print(str2)
# \t means tab daker print karna \n next line

str1 = "Welcome to my blog"                   
str2 = "Welcome to my \n Blog"
print(str1)
print(str2)
# \n sa next line

str1 = """ Welcome to my blog.This is for Class X"""
print(str1)
#triple qutes as it is print

str = "hello"
print(str[:3])
# slicing 

s = 'My'                        
s1 = 'Blog'                      
s2 = s[:1]+s1[len(s1)-1:]                        
print(s2)
# here we use slicing 

print("My"+'Blog' * 2)
# MyBlogBlog

print("My" *3 + "Blog" +'7')
# MyMyMyBlog7

for i in range(2,7,2):                
    print(i * '2')

for i in range(3,12, 2):                
    print("a".upper())

print(s.find('come'))              
print(s.find('o'))
print(s.find('o', 10, 20))
print(s.find('o', 5, 10))
# -1

str = "muskan"
c = 0
for i in str:
    c += 1
print(c)

i = 0
while str[i:]:
    i += 1
print(i)

# wethout len function we find the length

str1 = "Welcome to my Blog"
for i in str1:
    print(i)
    print(i, end =' ')
    print(i, end = '#')

str1 = "Muskan"
for i in str1:
    print(i)
    print(i, end =' ')
                                                                                                                                       
                                                         


