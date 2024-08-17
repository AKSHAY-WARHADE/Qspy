# Printing the no of digits as it is for upto a four digit number
# a=4567
# while a>0:
#     if a<100:
#         if a<10:
#             print(a)
#             break;
#         else:
#             b=a//10
#             print(b)
#             a %= 10
#     elif a<1000:
#         b=a//100
#         print(b)
#         a%=100
#     else:
#         b=a//1000
#         print(b)
#         a%=1000
#




# Chat Gpt code works with any number:
# def print_digits(n):
#         # Find the highest power of 10 less than or equal to n
#         power_of_ten = 1
#         while n // power_of_ten >= 10:
#             power_of_ten *= 10
#
#         # Print digits one by one
#         while power_of_ten > 0:
#             digit = n // power_of_ten
#             print(digit)
#             n %= power_of_ten
#             power_of_ten //= 10
#
#
#     # Example usage
# number = 85963575
# print_digits(number)

#Q1.Total No of Digits in n

#By using built in method i.e  Len and Str    #Works with positive as well as negative(jus have tu substract len-1)
# s=int(input("Enter the value"))
# print(len(str(s)))

#Without using built in methods     #Works with positiive values only, to avoid we can go with abs()
# s=int(input("Enter the value"))
# c=0
# while s>0:
#     s = s // 10         #c+=1
#     c+=1                #s = s // 10
# print(c)



#Q2.Reversing a number

#Using built in method and type casting
# n=eval(input("Enter a number"))
# print((str(n)[::-1]))

#Without using built in
# n=int(input("Enter a number"))
# res=0
# while n>0:
#     rem=n%10
#     res=res*10+rem
#     n //= 10
# print(res)



#Q3.Number palindrome

# n=int(input("Enter a number"))
# #without using built in
# res=0
# temp=n
# while n>0:
#     rem=n%10
#     res=res*10+rem
#     n //= 10
# if temp==res:
#     print(f"{temp} is a palindrome")
# else:
#     print(f"{temp} is not a palindrome")



#Q4. Count Zero,Even,Odd in a number
# n=int(input("Enter a number"))
# c,e,o=0,0,0
# if n>0:
#     while n>0:
#         rem=n%10
#         if rem==0:
#             c+=1
#         elif rem%2==0:
#             e+=1
#         else:
#             o+=1
#         n//=10
# elif n==0:
#     c+=1
#
# print(f"Total no of Zero: {c}, \nEven:{e},\nOdd:{o}")


#Q5. Sum of Even and Odd
#without using built in
# n=int(input("Enter a number"))
# se,so=0,0,
# if n>0:
#     while n>0:
#         rem=n%10
#         if rem%2==0:
#             se=se+rem
#         else:
#             so=so+rem
#         n//=10
# elif n==0:
#     print("Zero value entered")
#
# print(f"Sum of Even:{se}\nSum of Odd:{so}")


#Q6. Finding Max and Min in number
# n=int(input("Enter a number"))
# max=0
# min=9
# while n>0:
#         rem=n%10
#         if rem>max:
#             max=rem
#         elif rem<min:
#             min=rem
#         n//=10
#
# print(max)
# print(min)


#7  fibonacci series
# n=int(input("Enter a number"))
# a,b=0,1
# i=0
# while i<n:
#         print(a,end="")
#         c=a+b
#         b=a
#         c=b
#         i+=1


#8 Strong No
# n=int(input("N: "))
# sum=0
# temp=n
# while n>0:
#     rem=n%10
#     f=1
#     for i in range(1,rem+1):
#         f*=i
#     sum+=f
#     n//=10
# if temp==sum:
#     print(f"{temp} is a strong number")
# else:
#     print(f"{temp} is not a strong number")



