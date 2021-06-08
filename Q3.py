# year=int(input("enter a year="))
# if year%4==0:
#     if year%100!=0:
#         print("leap year")
# else:
#     print("not a leap year")

def is_leap(year):
    
    if year%4==0 and year%100!=0  or year%400==0:
        return True 
    else:
        return False
    
year = int(raw_input())
print (is_leap(year))