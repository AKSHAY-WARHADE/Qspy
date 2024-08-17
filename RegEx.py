import re

name="Akshay Warhade"
# a=re.match("Akshay",name)
# print(a)
# print(a.start())
# print(a.end())
# print(a.group())

# op:
# <re.Match object; span=(0, 6), match='Akshay'>
# 0
# 6
# Akshay

# b=re.fullmatch("Akshay Warhade",name)
# print(b)
# b1=re.fullmatch("Akshay Warhad",name)
# print(b1)

# op:
# <re.Match object; span=(0, 14), match='Akshay Warhade'>
# None


# c=re.search("s",name)
# print(c)
# c1=re.search("z",name)
# print(c1)

# op;
# <re.Match object; span=(2, 3), match='s'>
# None

# d=re.sub("s","$",name,count=1)
# print(d)
# d1=re.sub("z","$",name,count=1)
# print(d1)

# op:
# Ak$hay Warhade
# Akshay Warhade


# e=re.subn("k","!",name)
# print(e)
# e1=re.subn("z","!",name)
# print(e1)

# op:
# ('A!shay Warhade', 1)
# ('Akshay Warhade', 0)


# f=re.split("h",name,2)
# print(f)
# f1=re.split("z",name,1)
# print(f1)
#
# op:
# ['Aks', 'ay War', 'ade']
# ['Akshay Warhade']


# g=re.findall('[a-z]',name)
# print(g)
# g1=re.findall('[A-Z]',name)
# print(g1)
# g2=re.findall("[0-9]",name)
# print(g2)


# op:
# ['k', 's', 'h', 'a', 'y', 'a', 'r', 'h', 'a', 'd', 'e']
# ['A', 'W']
# []


#########################Assignment Questions##########################
# Q1
# a='The Cost of the book is Rs.100'
# x=re.findall('[0-9]',a)
# print(x)
# x1=re.findall(r'\d',a)
# print(x1)
# x2=re.findall('[0-9]+',a)
# print(x2)
# x3=re.findall(r'\d+',a)
# print(x3)


# # Q2
# b="hello HOW ARE YOU"
# a=[]
# d=[]
# for i in b:
#     if i.isupper():
#         a.append(i)
#     elif i.islower():
#         d.append(i)
# print(a,d)
#
# x=re.findall('[A-Z]',b)
# print(x)
# x1=re.findall('[A-Z]+',b)
# print(x1)


# Q3
# c="HELLO world welcome to python Hi how are you. Hi how are you"
# x=re.findall(r'\s',c)
# print(x)
# x1=re.findall("[' ']",c)
# print(x1)
# x2=re.findall(r'\W',c)
# print(x2)

#Q4
# word="PYTHON12nREG567exp2"
# x=re.findall(r'[0-9]',word)
# print(x)
# sum=0
# for i in x:
#     sum=sum+int(i)
# print(sum)


# Q5
# a="The cost of the book is Rs.100"
# x=re.findall(r'\D',a)
# print(x)


# Q6
# b="abcdefghijklmnop"
# x=re.findall('[e-z]',b)
# print(x)

#Q7
# word="@hello12world34welcome!123"
# x1=re.findall(r'\D',word)
# print(x1)

# Q8
# s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
# x=re.findall(r'[a-z]+\.[a-z]+',s)
# print(x)

#Q9
# s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
# x=re.findall(r'\b\d+',s)
# print(x)
# x1=re.findall(r'^[A-Z]+[0-9]+',s)
# print(x1)

#Q10
# s="my aadhar number is 1234-4567-8910"
# x1=re.findall(r'[0-9]+[-]+[0-9]+[-]+[0-9]+',s)
# print(x1)

#Q11
# a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
# x=re.findall(r'[A-Z]+[0-9]+[A-Z]',a)
# print(x)

# Q12
# a="https://www.google.com"
# x=re.findall('.+',a)
# print(x)
# x=re.findall(r'\w+',a)
# print(x)
# x1=re.findall(r'\w+[:]+[//]+\w+\.+\w+\.+\w+',a)
# print(x1)

# Q13
# file_format=["Graphic Interchange Format",
#               "Advanced Audio Coding",
#             "HyperText Markup Language",
#              "Content Management System",
#             "Windows Media,Audio",
#             "Comma Separated Values"]
# for i in file_format:
#     x=re.findall(r"[A-Z]",i)
#     print(x)
#     print(''.join(x))

# Q14
# emails=["test.user@company.gov","test_user@company.edu","123test-T.user@company.in","testing@company","pspider@company.in"]
# for i in emails:
#     x=re.findall(r'.+',i)
#     x1=re.findall(r'\w\.\w"@"\w\.\w{3}',i)
#     print(x1)