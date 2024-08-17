#
# a=lambda b: f"{b} is an even number" if b%2==0 else f"{b} is and odd number and reverse : "+(str(b)[::-1])
# print(a(39))


#1 find square and  cube
# a=lambda b: (b**2,b**3)
# print(a(10))

#2 palindrome
# a=lambda b:f"{b} is a Plaindrome" if b==b[::-1] else f"{b} is not a palindrome"
# print(a("Akshay"))

#3 negative to positive
# a=lambda b: abs(b) if b<0 else f"{b} is a positive no"
# print(a(-23))

#4  return key
# a={"hello":"Sony","How":"are","you":"bye"}
# x=lambda b: b.keys()
# print(x(a))


#5 evenodd
# a=lambda b:f"{b} is an even number"if b%2==0  else f"{b} is an odd number"
# print(a(20))


#6 return first element of sequence
# a=lambda b: b[0]
# print(a("Hello"))


#7 len of iterable
# a=lambda b: len(b)
# print(a([1,2,3,4]))
# print(a("Hello"))


#8 list of squares
# l=[2,3,4,5,6]
# a=lambda b: [b[i]**2 for i in range(0,len(b))]
# print(a(l))


#9 palindrome
# l=["nayana","kayak","mom","school","bag","dad"]
# a= lambda b:[b[i] for i in range(0,len(b)) if b[i]==b[i][::-1]]
# print(a(l))


#10 print numbers in list with corresponding list indices
# l=[100,200,300,400,500]
# a=lambda b:[(i,b[i]) for i in range(0,len(b)) ]
# print(a(l))


#11 check sequence datatype
# a=lambda b: (len(b),b) if isinstance(b,(str,list,tuple)) else (type(b),b)
# print(a((1,2,3)))


#12 divisible by 5 and 3
# a=lambda b: f"{b} is divisible" if b%3==0 and b%5==0 else f"{b} is not divisible"
# print(a(15))


#13 if even return square or else square root
# a=lambda b: b**2 if b%2==0 else b**0.5
# print(a(15))


# #14 if length even as it is else reverse
# a=lambda b:b if len(b)%2==0 else b[::-1]
# print(a("Hello"))

#15 wap to check length of given string and return value and length in tuple and dictionary
# a= lambda b:((b,len(b)),{b:len(b)})
# print(a("Hello"))