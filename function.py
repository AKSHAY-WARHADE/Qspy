#Wap to print good afternoon message
# def Greet():
#     print("Good Afternoon")
#
# Greet()

# def even_odd():
#     a=int(input("Enter a Number"))
#     if a%2==0:
#         print(f"{a} No is even")
#     else:
#         print(f"{a} is an odd number")
#
# even_odd()


# def even_odd(a):
#     if a%2==0:
#         print(f"{a} is even")
#     else:
#         print(f"{a} is odd")
# even_odd(10)
# even_odd(25)


# def pal():
#     name=eval(input("Enter a value"))
#     if name==name[::-1]:
#         return True
#     else:
#         return False
# x=pal()
# print(x)

# def palindrome(x):
#     if x==x[::-1]:
#         print(f"{x} is a palindrome")
#     else:
#         print(f"{x} it is not a palindrome")
# palindrome("MOM")


# x=["Walmart","Amazon","India","Snapchat","Meta","Google"]
# def check(x):
#     s=[]
#     for i in x:
#         if len(i)%2==0:
#             s.append(i)
#     return s
# print(check(x))

# def ret(a,b):
#     return a+b,a-b,a*b
# print(ret(10,20))






#Type of Arguments:-


# #positional arguments
# def add(a,b):
#     print(a+b)
# add(10,20)
# add()#error
# add(23,25,45)#error


#Variable Positional Arguments(*args):
# def add(*args): #return type of args is tuple
#     print(args)
#     print(*args)#unpacking
# add({1,34,45,34},"hello",34+67j)
# add()#Noerror


#Keyword Positional Arguments(=)
# def add(a,b):
#     print(a+b)
# add(a=10,b=20)#keyword positional arguments assigned using = symbol


#Variabe Keyword Arguments (**kwargs):
# def add(**kwargs):   #return type of kwargs is dictionary
#     print(kwargs)
# add(a=1,b=34,c=45,d=90) #We can pass multiple arguments and the variablename should be alphabetic

#Combination Arguments
# def combinations(*args,**kwargs):
#     print(args,kwargs)
# combinations(1,2,3,a=10,b=90,c=89)


