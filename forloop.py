#Prog1
# s="Akshay"
# for i in s:
#
#     print(i, end=" ")
#

# s=["a","e","i","o","u"]
# for i in s:
#     print(i,end=" ")

#
# s=(1,3,4,67,89)
# for i in s:
#     print(i, end=" ")

#
# s={1,23,45,67}
# for i in s:
#     print(i,end=" ")

#
# s={"a":123,"b":456,"c":789}
# for i in s.items():
#     print(i, end=" ")


# s=str(input("Enter a string"))
# for i in s:
#     if len(s)==6:
#         print(i)



# #120 to143
# for i in range(120,144,1):
#     print(i)


#Prog1
# l1=[]
# l2=[]
# for i in range(1,21,1):
#     if i%2==0:
#         l1.append(i)
#
#     else:
#         l2.append(i)
#
# print(l2)
# print(l1)



#Prog2
# s="hello123"
# l1=[]
# l2=[]
# for i in s:
#     if i.isalpha() and i in "aeiou":
#         l1.append(i)
#     if i.isdigit():
#         l2.append(i)
# print(l1)
# print(l2)



#Prog3
# l=["vaidehi","rahul","shivam","kapil","patil"]
# for  i in l:
#     s=i.capitalize()
#     print(s)


#Prog4
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if type(i) in (int,float,bool,complex):
#         print(i)



#Prog5
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# s=0
# for i in l:
#     if isinstance(i,(int,float,bool,complex)):
#         s+=i
# print(s)


# l="programming day"
# l1=[]
# l2=[]
# for i in range(len(l)):
#     l1.append(l[i])
#     l2.append(i)
# print(l1)
# print(l2)

#Enumerate
# l="programming day"
# a=enumerate(l)
# print(list(a))


# l="programming day"
# for i in enumerate(l):
#     print(i)


# #Reversed
# l="programming day"
# print(list(reversed(l)))

# a="programming"
# for i in reversed(a):
#     print(i)

#Zip
# l="programming day"
# s="Hello  buddy"
# print(list(zip(l,s)))

# l="programming day"
# s="Hello  buddy"
# for i in zip(l,s):
#     print(i)



#Zip longest
# l="programming day"
# s="hello"
#from  itertools import zip_longest
# print(list(zip_longest(l,s,fillvalue="hi")))

# from  itertools import zip_longest
# l="programming day"
# s="hello"
# for i in zip_longest(l,s,fillvalue=100):
#     print(i)





#Prog6
# s="india got independance in the year 1947"
# l=[]
# a=[]
# d=[]
# for i in s:
#     if i.isalpha():
#         l.append(i)
#     elif i.isdigit():
#         d.append(i)
#     elif i.isspace():
#         a.append(i)
#     else:
#         print("invalid")
#
# print(len(l),l)
# print(len(a),a)
# print(len(d),d)

#Prog7
# s="hello world sentence"
# s=s.strip()
# count=0
# for i in s:
#     if i.isspace():
#         count+=1
#
# print("No of words = ",count+1)



#Prog8
# s="hello world"
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)


#Prog9
# names=["apple","google","yahoo","microsoft","gmail","walmart","hello"]
# c=dict(zip(names,names))
#
# for i in c:
#     if len(i)%2==0:
#         print(c)
#     else:
#         pass



#reverse list
# s=[1,2,3,4]
# res=[]
# for i in s:
#     res=[i]+res
# print(res)

#Prog13
# s="you did it guys"
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)


#Prog9
# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# d={}
# for i  in names:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)


#Prog11
# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)


#Prog12
# s="Never Give Up"
# l=0
# for i in s:
#     l+=1
# print(l)

#Prog13
# s="hello  python"
# for i in range(0,len(s),2):
#     print(s[i],end="")


#Prog10
# n=int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)


#Prog15
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=i.index(i)
# print(d)


#Prog16
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=len(i)
# print(d)


#Prog17
# s="sunday"
# d={}
# for i in s:
#     d[i]=i.upper()
# print(d)

# s="sunday"
# d={}
# for i in s:
#     d[i]=chr(ord(i)-32)
# print(d)

#Prog18
# l=[89,51,111,77,108,120]
# d={}
# for i in l:
#     d[i]=chr(i)
# print(d)


#Prog19
# s="sunday"
# l=[]
# for i in s:
#     l=(i,ord(i))
#     print(l, end="")


#Prog20
# lst= ['hai', 'hello', 'python', 'world', 'jingalala']
# for i in lst:
#     lst*=0
# print(lst)

#Prog21
# s="Today is Tuesday and attending python session"
# d={}
# for i in s.split():
#     if i[-1] in ("a","e","i","o","u","y"):
#         d[i]=len(i)
# print(d)

# s="Today is Tuesday and attending python session"
# d={}
# for i in s.split():
#     if i.endswith (("a","e","i","o","u","y")):
#         d[i]=len(i)
# print(d)


#Prog22
#
# s="hi hello good morning welcome to python session"
# d={}
# for i in s.split():
#     if i[0] not in d:
#         d[i[0]]=[i]
#
#     else:
#      d[i[0]] +=[i]
# print(d)


#Prog23
# s="hello python"
# d={}
# for i in range(0,len(s)):
#     if s[i] not in d:
#         d[s[i]]=[i]
#     else:
#        d[s[i]] +=[i]
# print(d)


#Prog24
# s="tomorrow is weekend and non-veg special"
# d={}
# for i in s.split():
#     d[i]=i[::-1]
# print(d)


#Prog25
# s=[1,2,3,4]
# res=[]
# for i in s:
#     res=[i]+res
# print(res)



#Prog 26
# s = 'Sony12India567pvt21ltd'
# sum=0
# for i in range(0,len(s)):
#     if s[i].isdigit():
#         sum=sum+int(s[i])
# print(sum)


#Prog27
# l = [1, 2, 3, 4, 6, 7, 10]
# for i in range(1,10):
#     if i not in l:
#         l.append(i)
#
# print(l)


#Prog28
# d=[1,2,3,4,5,6,7,1,2,3,4]
# for i in d:
#     if d.count(i)>1:
#         d.remove(i)
# print(d)
#
# d=[1,2,3,4,5,6,7,1,2,3,4]
# dup=[]
# nondup=[]
# for i in d:
#     if i not in nondup:
#         nondup.append(i)
#     else:
#         dup.append(i)
# print(dup)
# print(nondup)


#Prog29:
# s="hellohai"
# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,"-")
# print(s)


#Prog30
# l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3],True, (1,3,7), 6+3j]
# l2=[]
# for i in range(0,len(l)):
#     if isinstance(l[i],(int,float,complex)):
#         l2.append(l[i])
#     elif isinstance(l[i],(list,tuple,set)):
#         l2.extend(l[i])
#     elif isinstance(l[i],(bool,str)):
#         l2
# print(l2)


#Prog31
# a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
# for i in a:
#     print(i[0],i[-1])



#Prog32
# b=[2,4,5,6,7,1]
# l=[]
# for i in b:
#     l.append(i**2)
# print(l)


#Prog33
# c=[2,4,5,3,7,9]
# l=[]
# for i in c:
#     if i%2==0:
#         l.append(i**2)
#     else:
#         l.append(i**3)
# print(l)



#Prog34
# d=[2,4,5,1,8,9,10]
# l=[]
# s=0
# c=0
# for i in d:
#     s=i**2
#     c=i**3
#     l.append((s,c))
# print(l)


#Prog35
# names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
# l=[]
# for i in names:
#     l=list(reversed(names))
# print(l)

#Prog36
# data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
# ind = []
# coll =[]
# for i in data:
#     if isinstance(i,(int,float,complex,bool)):
#         ind.append(i)
#     else:
#         coll.append(i)
#
# print(ind)
# print(coll)

#Prog37
# books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}
# for i in books.values():
#
#     print(i[0])


#Prog38
# char=["a","M","i","A","M","I","i","H","a","H"]
# d={}
# for i in char:
#     d.update({i:char.count(i)})
# print(d)

#Prog39
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
#
# from itertools import zip_longest
# a=zip_longest(d,p)
# print(list(a))

#Prog40
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
# for i in zip(d,p):
#     if len(i[0])%2==0:
#         print(i)


#Prog41
# l1=[10,20,30,40]
# l2=[78,44,11,99]
# l3=[1,2,3,4]
# for i in zip(l1,l2,l3):
#         print(sum(i))

#Prog42
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}
# for i in zip(d.values(),p.values()):
#     print(i)

#Prog43
# l = [[1,2,3], [4,5,6], [7,8,9]]
# l2=[]
# l3=[]
# internal=0
# external=0
# for i in l:
#     l2.extend(i)
#     l3.extend(l)
#     internal = sum(i)
#     print(internal,end=" ")
# external=sum(l2)
# print("\n",external)


#
# l = [[1,2,3], [4,5,6], [7,8,9]]
# l2=[]
# for i in l:
#     internal=0
#     for j in i:
#         internal+=j
#     l2.append(internal)
# print(l2)
# external=0
# for k in l:
#     for m in k:
#         external+=m
# print(external)


#Prog44

# l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# d={}
# for i in l:
#     a=i.split()
#     if a[1] not in d:
#         d[a[1]]=[a[0]]
#     else:
#         d[a[1]]+=[a[0]]
#
# print(d)



