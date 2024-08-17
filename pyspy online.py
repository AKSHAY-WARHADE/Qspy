#Swapping Program(Temp Variable)
#Method1(Works with any datatype)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b}")
# c=a+b
# b=c-b
# a=c-a
# print(f"After Swapping \n a:{a} \n b:{b}")


#Method2(Works with any datatype)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b}")
# a=a+b
# b=a-b
# a=a-b
# print(f"After Swapping \n a:{a} \n b:{b}")


#Method3- Multiplication and Floor division(Not Possible with 0)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b}")
# a=a*b
# b=a//b
# a=a//b
# print(f"After Swapping \n a:{a} \n b:{b}")


#Method4- EXR Operation(Only for Integers)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b}")
# a=a^b
# b=a^b
# a=a^b
# print(f"After Swapping \n a:{a} \n b:{b}")


#Method5(,operator) for any datatype
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b}")
# a,b=b,a
# print(f"After Swapping \n a:{a} \n b:{b}")


#Swapping 3 Numbers(Temp variable)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b} \n c:{c}")
# d=a
# a=c
# c=b
# b=d
# print(f"After Swapping \n a:{a} \n b:{b} \n c:{c}")

#Method 2(+,-)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b} \n c:{c}")
# a=a+b+c
# b=a-b-c
# c=a-b-c
# a=a-b-c
#
# print(f"After Swapping \n a:{a} \n b:{b} \n c:{c}")

#Method 3(*,//)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b} \n c:{c}")
# a=a*b*c
# b=a//b//c
# c=a//b//c
# a=a//b//c
#
# print(f"After Swapping \n a:{a} \n b:{b} \n c:{c}")



#Method 4(^ EOR)
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# print(f"Before Swapping \n a:{a} \n b:{b} \n c:{c}")
# a=a^b^c
# b=a^b^c
# c=a^b^c
# a=a^b^c
#
# print(f"After Swapping \n a:{a} \n b:{b} \n c:{c}")

#EvenOdd(If else)
# n=int(input("N:"))
# if (n//2)*2==n:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")

# n=int(input("N:"))
# if (n//2)*2==n-1:
#     print(f"{n} is Odd")
# else:
#     print(f"{n} is Even")

# Bitwise Operator
# n=int(input("N:"))
# if n&1==0:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")





#Nested For(Pattern Programming)
# for i in range(1,3):
#     for j in range(1,4):
#         print(i*j,end=" ")
#
# a=int(input("Enter the Number of rows"))
# for i in range(a):
#     print("*")




#Steps:
"""
1) Controlling No of Rows
2) Controlling No of Columns
3) Empty Print(Outside Nested Loop)
"""
# Rectangle or Square Pattern
# a=int(input("Enter the Number of Rows: "))
# b=int(input("No of Columns: "))
# for i in range(a):
#     for j in range(b):
#         print("*",end=" ")
#   print()





# a=int(input("Enter the Number of Rows: "))   o/p:- 1111
# b=int(input("No of Columns: "))                    2222
# for i in range(1,a):
#     for j in range(b):
#         print(i,end=" ")
#     print()

# a=int(input("Enter the Number of Rows: ")) o/p: same as above
# b=int(input("No of Columns: "))
# val=1
# for i in range(1,a):
#     for j in range(1,b):
#         print(val,end="")
#     print()
#     val+=1


# a=int(input("Enter the Number of Rows: "))
# b=int(input("No of Columns: "))
# for i in range(a):
#     val = 1
#     for j in range(b):
#         print(val,end="")
#         val+=1
#     print()

"""o/p:12345
       12345
       12345"""


# a=int(input("Enter the Number of Rows: "))
# b=int(input("No of Columns: "))
# for i in range(a):
#     val = 1
#     for j in range(b):
#         print(val,end="")
#         val+=1
#         if (val>9):
#             val=1
#     print()

"""Op:
123456789123
123456789123
123456789123"""

# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# val=row
# if val>9:
#     val=9
# for i in range(row):
#     for j in range(col):
#         print(val,end="")
#     print()
#     val-=1
#     if  val<1:
#         val=9

"""
Enter the Number of Rows: 11
No of Columns: 5
99999
88888
77777
66666
55555
44444
33333
22222
11111
99999
88888


"""

# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# for i in range(row):
#     val=col
#     for j in range(col):
#         print(val,end=" ")
#         val-=1
#     print()



# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# val=ord("A")
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#     print()
#     val+=1

"""
Enter the Number of Rows: 4
No of Columns: 4
A A A A 
B B B B 
C C C C 
D D D D 



"""


# row=int(input("Enter the Number of Rows: "))
# col=int(input("No of Columns: "))
# val=ord("A")
# for i in range(row):
#     for j in range(col):
#         print(chr(val),end=" ")
#     print()
#     val+=1
#     if val>ord("Z"):
#         val=ord("A")
#
"""
Enter the Number of Rows: 27
No of Columns: 4
A A A A 
B B B B 
C C C C 
D D D D 
E E E E 
F F F F 
G G G G 
H H H H 
I I I I 
J J J J 
K K K K 
L L L L 
M M M M 
N N N N 
O O O O 
P P P P 
Q Q Q Q 
R R R R 
S S S S 
T T T T 
U U U U 
V V V V 
W W W W 
X X X X 
Y Y Y Y 
Z Z Z Z 
A A A A """

#
# row=int(input("Enter No of Rows"))
# col=int(input("Enter No of Columns"))
# for i in range(row):
#     val=ord("A")
#     for j in range(col):
#         print(chr(val),end=" ")
#         val+=1
#         if val>ord("Z"):
#             val=ord("A")
#     print()
"""
Enter No of Rows5
Enter No of Columns28
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
"""


"""
homework
1:
ccc
bbb
aaa

2:
cba
cba
cba
"""



#Pyramids
# n=int(input("Enter The No of Rows"))
# star=1
# spc=n-1
# for i in range(n):
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(star):
#         print("*",end=" ")
#     print()
#     star+=2
#     spc-=1


#2nd Way
# n=int(input("Enter The No of Rows"))
# star=1
# spc=n-1
# for i in range(n):
#     print(" "*spc+"*"*star)
#     star+=2
#     spc-=1

#3rd Way
#star 2*i+1
#spc n-1-i
# n=int(input("Enter The No of Rows"))
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()

#4th Way
# n=int(input("Enter The No of Rows"))
# for i in range(n):
#     print("  "*(n-1-i)+"* "*(2*i+1))

#Number Pyramid
# n=int(input("Enter The No of Rows"))
# star=1
# spc=n-1
# val=1
# for i in range(n):
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(star):
#         print(val,end=" ")
#     print()
#     star+=2
#     spc-=1
#     val+=1

# 2nd Way
# n=int(input("Enter The No of Rows"))
# val=1
# for i in range(n):
#     print("  "*(n-1-i)+(str(val)+" ")*(2*i+1))
#     val+=1
#     if val>9:
#         val=1

#Alphabet
# n=int(input("Enter The No of Rows"))
# val=ord("A")
# for i in range(n):
#     print("  "*(n-1-i)+(chr(val)+" ")*(2*i+1))
#     val+=1

#Alphbet Incerement
# n=int(input("Enter The No of Rows"))
# star=1
# spc=n-1
# for i in range(n):
#     val = ord("A")
#     for j in range(spc):
#         print(" ",end=" ")
#     for k in range(star):
#
#         print(chr(val),end=" ")
#         val += 1
#     print()
#     star+=2
#     spc-=1

Assignment Side Pyramid and Inverted Pyramid
