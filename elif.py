###
# a=eval(input("Enter  a Number"))
# if a>0:
#     print("It is a positive number")
# elif a==0:
#     print("It is  a neutral number")
# else:
#     print("It is a negative number")


#Prog1
# s=eval(input("Enter the characters"))
# if ord("A")<=ord(s)<=ord("Z"):
#     print("its upperacse")
# elif ord("a")<=ord(s)<=ord("z"):
#     print("its a lowercase")
# elif ord("0")<=ord(s)<=ord("9"):
#     print("its a digit")
# else:
#     print("its a special character")



#Prog2
# s=eval(input("Enter the data"))
# if type(s) in (list, tuple, str):
#     print("it is an sequence")
# elif type(s) in (int, float, complex, bool):
#     print("its a individual")
# else:
#     print("its a iterable")


#Prog3
# a=eval(input("Enter data"))
# if type(a)==str:
#     print(len(a))
# elif type(a)==list:
#     print(a.pop())
# elif type(a)==tuple:
#     print(a[::-1])
# else:
#     print("Invalid")


#Prog 4
# age=int(input("Enter your age"))
# if 0<=age<=17:
#     print("child")
# elif 18<=age<=30:
#     print("You are Adult")
# elif 31<=age<=60:
#     print("Your are men")
# elif 61<=age<=100:
#     print("senior citizen")
# else:
#     print("Invalid")



#Prog5
# d=eval(input("enter your  joining year"))
# exp=2024-d
# if 0<=exp<=2:
#     print("No Hike")
# elif 3<=exp<=5:
#     print("5000 rs Hike")
# elif 6<=exp<=8:
#     print("7000  rs Hike")
# else:
#     print("10000 rs hike")



#Prog6
# a=65
# b=34
# c=76
# if a<b and c:
#     print("A is smallest")
# elif b< a and c:
#     print("B is smallest")
# else:
#     print("Z is smallest")



#Prog7
# m=eval(input("Enter marks of 5 subjects"))
# a=sum(m)/5
# if 90<=a<=100:
#     print("Distinction")
# elif 75<=a<=89:
#     print("First Class")
# elif 60<=a<=74:
#     print("Second Class")
# elif 50<=a<=59:
#     print("Third Class")
# else:
#     print("fail")


#Prog8
# h=float(input("enter height of students"))
# if h>=6.0:
#     print("Stand Last in line")
# elif 5.0<=h<=5.9:
#     print("stand at second last")
# elif 4.0<=h<=4.9:
#     print("Stand in between")
# else:
#     print("Stand in front")



#prog9
# age=int(input("Enter your age"))
# g=str(input("Enter your Gender"))
#
# if age>18 and g in ("female","f"):
#     print("You are a girl and eligible for marriage")
# elif age>21 and g in ("male", "m"):
#     print("You are a male and you are eligible  for marriage")
# elif age<18 and g in ("female","f"):
#     print("You are a girl and you are not eligible for marriage")
# elif age<21 and g in ("male", "m"):
#     print("You are a man and you are not eligible for marriage")
# else:
#     print("You are not eligible for marriage")



#prog 10
# p=eval(input("Enter the price of elements"))
# p=sum(p)
# if 1000<=p<=3000:
#     print("Discount 500")
# elif 3001<=p<=5000:
#     print("discount 1000")
# elif p>=5001:
#     print("discount 1200")
# else:
#     print("Nodiscount")


#prog11
# a=int(input("Enter a number"))
# if a%2==0:
#     print("Even")
# elif a%2==1:
#     print("odd")
# elif a==0:
#     print("zero")
# else:
#     print("invalid")



#Prog12
# color=["red","yellow","green"]
# a=str(input("enter the signal color"))
#
# if a in color and a=="red":
#     print("Stop")
# elif a in color and a=="yellow":
#     print("Get Ready")
# elif a in color and a=="green":
#     print("Move")
# else:
#     print("invalid color")
