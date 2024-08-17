# a=int(input("enter a number"))
#
# if a%2==1:
#     print(f"The given number {a} is odd number")
#



# a=int(input("Enter a number"))
#
# if a%2==0:
#     print(f"The entered number {a} is Even")


# percent=float(input('The the student percentage '))
#
# if percent>=70:
#     print(f'Good Luck')


# a=98
# b=67
# if a>b:
#     print(f'The {a} is greater')


#
# s="hey guys you all are Osam"
# if len(s)%2==0:
#     print(f"the length of the given string {s} is even")
# print(len(s))




# a=int(input("enter a number"))
#
# if a%5==0:
#     print(f'the given no {a} is divisible by 5')




# p=["java","python","c","c++","RuBy","golang"]\
#
# if type(p)==list:
#     print(f"the given input {p} is a list")




#
# age=int(input("Enter your age"))
# if age>=18:
#     print(f"The person with age {age} is eligible for vote")





# num=int(input("Enter a number negative ofr positive"))
#
# if num>=0:
#     print(f'The entered no {num} is positive')



# a=str(input("Enter a string"))
#
# if (a[0::]==a[::-1]):
#     print(f'the input string {a} is palindrome')
#
#


# s='Lahari is a good student'
# if s[0::] in ("a","e","i","o","u","A","E","I","O","U"):
#     print(f"The first letter of the given string is consonant")
#

#
# a=str(input('Enter a string'))
# if a==a.upper():
#     print(f"the given string {a} is in uppercase format")



# a=eval(input('enter some data '))
# if type(a)==str:
#     print(f'the given input {a} is string')
#


# a=int(input('Enter a no'))
#
# if a>1 and a<5:
#     print("Python coding")



# a=int(input("Enter a number"))
#
# if a<0:
#     print(f"Its a negative number")
#




# x=int(input("Enter a number"))
# if  x%2==0 and x%6==0:
#     print(f"The given no {x}is divisible")
#     print(complex(x))


# x=int(input('enter a number'))
# l=[1,3,4]
# if x%2==0:
#     l.append(x)
# print(l)


# x=int(input('enter a number'))
# l=[1,3,4]
# if x%2==0:
#     l+=[x]
# print(l)


#
# x=int(input('Enter a number'))
# if x%5==0 and x%7==0:
#     a=x*x
#     print(a)


#
# x=int(input('enter a number'))
# if x>=45 and x<=200 and x%4==0 and x%5==0:
#     print(chr(x))


#
# s1="hello world"
# s2="world"
# if s2 in s1:
#     print(f"the string {s2} is present in {s1} ")



#
# a=input("enter data")
# s={}
# if a.isalpha():
#     s[a]=ord("a")
#     print(s)


#
# a=input("Enter data")
# d={}
# if a.isupper():
#     a=a.lower()
#     d[a]=ord(a)
#     print(d)

a=str(input("Enter data"))
d={}
if ord(a)>=65 and ord(a)<=90:
    x=ord(a)+32
    d[chr(x)]=x
    print(d)

