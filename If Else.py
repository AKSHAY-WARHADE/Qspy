# #Prog 1
# a=int(input("enter a number"))
# if a%2==0:
#     print(f"The given number {a} is even number")
# else:
#     print(f"The number {a} is odd ")
#
#
#Prog 2
# g=str(input("Enter your Gender"))
# a=int(input("enter your age"))
#
# if g in ("male", "Male", "m", "M") and a>=26 or g in ("female","Female","f","F") and a>=24:
#     print(f"The person with gender {g}  and age {a} is eligible for wedding")
# else:
#     print(f"The person with gender {g}  and age {a} is not eligible for wedding")

#Prog 3
# s=str(input("enter a character"))
#
# if s.islower():
#     print(s.upper())
# else:
#     print(s)


# #Prog 4
# s=str(input("enter a character"))
#
# if s.isupper():
#     print(s.lower())
# else:
#     print(s)



#prog 5
# n1=34
# n2=54
# if n1>n2:
#     print(f"The number{n1} is greater than number {n2}")
# else:
#     print(f"The number {n2} is greater than number{n1}")



#prog 6
# n=int(input("Enter a number"))
# if n%2==0:
#     print(f"The number {n} is even")
# else:
#     n=n+1
#     print(n)


#Prog7
# s="python"
# if s[0].isupper():
#     print(s)
# else:
#     s=s.capitalize()
#     print(s)


#Prog 8

# x=int(input("enter a number"))
# if x%2==0:
#     x=x/2
#     print(x)
# else:
#     x= x**2
#     print(x)


#Prog 9
# x=int(input("Enter a number"))
#
# if x%3==0 and x%7==0:
#     print(f"the no {x} is divisible by 3 and 7")
# else:
#     print(f"the no {x} is  not  divisible by 3 and 7")



#Prog 10
# s=eval(input("Enter a string in quotes"))
# if len(s)%2==0:
#     s=s[::-1]
#     print(s)
# else:
#     s=s.upper()
#     print(s)



#Prog 11
# s=int(input("Enter a Number"))
# if s>=0:
#     print(f"The entered no {s} is Positive")
# else:
#     print(f"The entered number {s}is negative")



#Prog12
# s=eval(input("Enter some data"))
#
# if type(s) in ("int","float","complex","bool"):
#     print(f"The entered data is of individual type")
# else:
#     print(f"The entered data is of collection type")


#Prog 13
# e=str(input("Enter a character"))
# s="python"
# if e in s :
#     print(f"The entered character  is present in string")
# else:
#     print(f"The entered character  is  not present in string")


#Prog14
# D={"a":"apple","b":"ball","c":"cat"}
#
# if len(D)%2==0:
#     print(D)
# else:
#     D["d"]="Dog"
#     print(D)



#Prog15
# e=int(input("Enter a Number"))
# if e>5:
#     e=-abs(e)
#     print(e)
# else:
#     print(e)



#Prog16
# e=int(input("Enter a Number"))
# if e<10:
#     print(e ** 2)
# else:
#     print(e)



#Prog17
# e=int(input("Enetr a number"))
# if e%2==1:
#     x=divmod(e,2)
#     print(x)
# else:
#     print(f"the entered no {e} is even")


#Prog18
# r=str(input("Enter data"))
# if r.isalpha():
#     print(r*2)
# else:
#     print(f"The entered data is not alphabet")



#Prog19
# r=int(input("Enter an number"))
# if r%6==0:
#     r=r**3
#     print(r)
# else:
#     r=r<<3
#     print(r)