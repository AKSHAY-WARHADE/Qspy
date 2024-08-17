#List Compression
"""
syntax1-without using if and else
var_name=[expression for loop condition]

syntax2- with using only if
var_name=[TSB for loop condition if condition]

syntax3- with using if and else both
var_name=[TSB if condition else FSB for loop condition]

note: we can't create two separate variable using comprehension
"""
#Syntax1 without if and else condition
#x=[1,2,3,4,5,6]
# res=[]
# for i in x:
#     res.append(i**2)
# print(res)

#Compressed Format
#x=[i**2 for i in x]
#print(x)

#Without using seperate print
# print([i**2 for i in x])


#Syntax2 with if condition
# k=[]
# for i in x:
#     if i%2==0:
#         k.append(i)
# print(k)
#Compressed
# x=[i for i in x if i%2==0]
# print(x)



#Syntax3 with both if and else
# z=[]
# for i in x:
#     if i%2==0:
#         z.append(i**2)
#     else:
#         z.append(i**3)
# print(z)
#Compressed
# x=[i**2 if i%2==0 else i**3 for i in x]
# print(x)





#Set Comprehension
"""
syntax1-without using if and else
var_name={expression for loop condition}

syntax2- with using only if
var_name={TSB for loop condition if condition}

syntax3- with using if and else both
var_name={TSB if condition else FSB for loop condition}
"""
#Syntax1 without if and else condition
# x={1,2,3,4,5,6}
# res={}
# for i in x:
#     res.append(i**2)
# print(res)

#Comprressed Format
# x={i**2 for i in x}
# print(x)
#Without using seperate print
# print({i**2 for i in x})


#Syntax2 with if condition
# k={}
# for i in x:
#     if i%2==0:
#         k.append(i)
# print(k)
#Compressed
# x={i for i in x if i%2==0}
# print(x)



#Syntax3 with both if and else
# z={}
# for i in x:
#     if i%2==0:
#         z.append(i**2)
#     else:
#         z.append(i**3)
# print(z)
#Compressed
# x={i**2 if i%2==0 else i**3 for i in x}
# print(x)




#Dictionary Comprehension
"""
syntax1-without using if and else
var_name={key:value for loop condition}

syntax2- with using only if
var_name={key:value for loop condition if condition}

syntax3- with using if and else both
var_name={key:value if condition else FSB for loop condition}
"""
#Syntax1
# s="comprehension"
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)

#Compressed
# s={i:ord(i) for i in s}
# print(s)



#Syntax2
# y=[11,12,13,14,15]
# d={}
# for i in y:
#      if i%2==0:
#         d[i]=i**2
#
# print(d)

#Compressed
# y={i:i**2  for i in y if i%2==0}
# print(y)

#Syntax3
# y=[11,12,13,14,15]
# d={}
# for i in y:
#     if i%2==0:
#         d[i]=i
#     else:
#         d[i]=i**2
# print(d)

#Compressed
# y={i:i if i%2==0 else i**2 for i in y}
# print(y)



"""
Note:
When we use tuple for compression it will result a generator address 
which we have to type cast to get an output with set or list 
so  tuple comprehension is called as Generator Expression
"""


#List Example:
# l1=[]
# l2=[]
# for i in range(1,21):
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l1)
# print(l2)
# l1=[i  for i in range(1,21) if i%2==0]
# print(l1)




#Q1
# l=[2,32,1,52,31,24,56,75]
# l2=[]
# for i in l:
#     if i%2==0:
#         l2.append(i)
# print(l2)


# l=[i for i in l if i%2==0]
# print(l)


#Q2
# l=[2,3,5,1,7,2,3]
# l2=[]
# for i  in l:
#     if i%2==0:
#         l2.append(i**2)
#     else:
#         l2.append(i**3)
# print(l2)

# l=[i if i%2==i**2 else i**3 for i in l]
# print(l)

#Q3
# l=[]
# for i in range(1,21):
#     if i%2==0:
#         l.append(i)
# print(l)
# l=[i for i in range(1,21) if i%2==0]
# print(l)


#Q4
# l=[]
#a=int(input("Enter a number"))
# for i in range(1,11):
#     s=i*a
#     l.append(s)
# print(l)

# l=[i*a for i in range(1,11) ]
# print(l)


#Q5
# l1=eval(input("Enter a list"))
# l2=eval(input("Enter a list"))
# l3=[]
# for i in range(1):
#     a=l1+l2
# l3.append(a)
# print(l3)
# l1=[l1+l2 for i in range(1)]
# print(l1)


#Q6
#l=["hey","hello","good","evening","python"]
# a=[]
# for i in range(len(l)):
#     ab=(i,l[i])
#     a.append(ab)
# print(a)

# l=[(i,l[i]) for i in range(len(l))]
# print(l)


#Q7
#l=("hey","hello","good","evenings","python")
# a=[]
# for i in l:
#     if len(i)%2==0:
#         a.append(i)
#     else:
#         a.append(i[::-1])
# print(a)
# l=[i if len(i)%2==0 else i[::-1] for i in l]
# print(l)






#Dict Questions
#Q1
#l=[2,3,4,1,6,2,7,8,4]
# d={}
# for i in l:
#     d[i]=i**2
# print(d)
# l={i:i**2 for i in l}
# print(l)

#Q2
#l=["google","apple","python","orange"]
# d={}
# for i in range(0,len(l)):
#     d[l[i]]=i
# print(d)
# l={l[i]:i for i in range(0,len(l))}
# print(l)


#Q3
#l=["google","apple","python","orange"]
# d={}
# for i in l:
#     if len(i)%2==0:
#         d[i[1]]=i
# print(d)
# l={i[1]:i for i in l if len(i)%2==0}
# print(l)


#Q4
#l=["google","apple","python","orange"]
# d={}
# for i in l:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)
#l={i:i if len(i)%2==0 else i[::-1] for i in l}
#print(l)

#Q5
#l=["banana","malayalam","madam","sir","mom","dad"]
# d={}
# for i in l:
#     if i==i[::-1]:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)
# l={i:i if i==i[::-1] else i[::-1] for i in l}
# print(l)






#Set Comprehension
# l=[2,3,4,2,5,6,2,3]
# a={}
# for i in l:
#     if i not in a:
#         a={i,}
#     else:
#         i+=1
# print(a)

