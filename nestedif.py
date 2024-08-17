# Prog 1
# a=2
# if a%2==0:
#     print("Its an even number")
#     if a>=5:
#         print("Its is  greater in 5")
#     else:
#         print("Its is smaller than 5")
# else:
#     print("Its a odd number")



#Prog2
# a=35
# if a%2==1:
#     print("The num is odd")
#     if a%7==0:
#         print('it is divisible by 7')
#     else:
#         print("its is not divisible by 7")
# else:
#     print("its a even number")


#Prog3
# a=33
# if a%2==1:
#     print("The num is odd")
#     if a%7==0:
#         print('it is divisible by 7')
#     else:
#         print("its is not divisible by 7")
# else:
#     print("its a even number")



#Prog4
# username="python"
# password="python masters"
# a=str(input("Enter Your Username"))
# b=str(input("enter your password"))
#
# if a==username:
#     print("Username is correct")
#     if b==password:
#         print("Login Success")
#     else:
#         print("Wrong Password")
# else:
#     print("invalid  credentials")



#Prog5
# a=["city pride","pvr","inox","miraj"]
# print(f"Available Theaters: {a}")
# t=str(input("Enter the Theater Name"))
# if t in a:
#     print("Available Movies are\n")
#     print("bhaiyaji","chandu champion","house of dragons")
#     x=str(input("Enter the preferred movie name"))
#     if x == "bhaiyaji":
#         print(f"The ticket pricefor {x} is 200 rs")
#         p=int(input("Enter the amount"))
#         if p==200:
#             print("Ticket Booked Sussessfully")
#         else:
#             print("Payment unsuccessful")
#
#     elif x == "chandu champion":
#         print(f"The ticket pricefor {x} is 320 rs")
#         p = int(input("Enter the amount"))
#         if p == 320:
#             print("Ticket Booked Sussessfully")
#         else:
#             print("Payment unsuccessful")
#     elif x == "house of dragons":
#         print(f"The ticket pricefor {x} is 250 rs")
#         p = int(input("Enter the amount"))
#         if p == 250:
#             print("Ticket Booked Sussessfully")
#         else:
#             print("Payment unsuccessful")
#     else:
#         print("Enter a valid movie name")
#
#
# else:
#     print("Choose a valid theater")





#Prog 6
# s=[3,4,6,7,9,1,5]
# a=((len(s)-1)/2)
# print(a)
# print(s[3])
# if a%2==0:
#     print("the middle element is even")
# else:
#     print("the middle element is odd")




#Prog7
# apps=["flipkart","amazon"]
# c=["electronics","mobile","fashion","furniture"]
# print(f"Available apps: {apps}")
# f=str(input("enter the app name you want to use"))
# if f in apps:
#     a=str(input("enter the category of product you want to purchase"))
#     if a == "mobile":
#         print(f"You have chosen {a} category")
#         m=str(input("Enter a mobile name "))
#         if m in ["vivo","apple","samsung","oppo","oneplus"]:
#             print(f"You have choose {m} company mobile ")
#             print("Purchase Successful")
#         else:
#             print("Enter a valid company name")
#     else:
#         print(f"Enter a valid category among below {c}")
# else:
#     print("Enter a valid app name")



#Prog 8
# m=str(input("Enter the purchase mode"))
# if m== "credit card":
#
#     e=int(input("Enter the no of products you purchase"))
#     if e>=3:
#         a=float(input("Enter the total price of the products"))
#         if a >=500:
#             print("Congrats you got a discount of 10% on your purchase")
#             c= a*0.1
#             print("The effictive price will be :",c)
#         else:
#             print("Your product price should be greater than 500 to avail the discount")
#
#     else:
#         print("you have to purchase more products")
# else:
#     print("Have have choose different payment option so the discount can't be availed")



#Prog 9
# s=eval(input("Enter the list"))
# if type(s)==list:
#     a=["option1","option2","option3"]
#     e = str(input(f"chose the option from the list {a}"))
#     if e=="option1":
#         f=s.pop()
#         print(f)
#     elif e== "option2":
#         c=s.sort()
#         print(c)
#     elif e== "option3":
#         d = s.clear()
#         print(d)
#     else:
#         print("invalid option")
# else:
#     print("Invalid datatype")