# start=1
# while start<=10:
#     print(start)
#     start=start+1

# start=10
# while start>=1:
#     print(start)
#     start-=1

# start=0
# while start<=10:
#     print(start)
#     start+=2

# odd=[]
# even=[]
# start=1
# while start<=20:
#     odd.append(start)
#     start+=1
#     even.append(start)
#     start+=1
# print(odd)
# print(even)

# odd=[]
# even=[]
# start=1
# while start<=20:
#     if start%2==0:
#         even.append(start)
#     else:
#         odd.append(start)
#     start+=1
#
# print(odd)
# print(even)



# l=[1,2,17,49,50]
# sum=0
# i=1
# while i<len(l):
#     sum=sum+l[i]
#     i=i+1
# print(sum)


# s=65
# while s<=90:
#     print(chr(s))
#     s+=1

# start1=ord("A")
# start2=ord("a")
# while start1<=ord("Z") and start2<=ord("z"):
#     print(chr(start1),chr(start2),end="")
#     start1+=1
#     start2+=1


# s="Hello Python"
# i=1
# while i<len(s):
#     print(s[i],end='')
#     i+=2

#
# s=('Hello Python')
# i=0
# while i<len(s):
#     print(s[i],i,end=" ")
#     i+=1


# x=[1,2,3+4j,[1,2,3],'Hi',{1,2,3},3.7,True]
# i=0
# sum=0
# while i<len(x):
#     if isinstance(x[i],(int,float,bool,complex)):
#         print(x[i])
#         sum=sum+x[i]
#     i+=1
# print(sum)

# a=int(input("Enter a number"))
# i=1
# while i<11:
#     print(a,"*",i,"=",a*i)
#     i+=1


# n=[1,3+8j,'python',[1,2,3],{1,2,3},{7:9}]
# i=0
# while i<len(n):
#    if isinstance(n[i],list):
#        a=n.pop(3)
#        b=a+n
#        print(b)
#    i=i+1



# n=[1,3+8j,'python',[1,2,3],{1,2,3},{7:9}]
# i=0
# while i<len(n):
#     if i==3:
#         n.pop(i)
#         n.extend(n[i])
#     i+=1
# print(n)



# y='Hello123'
# i=0
# while i<len(y):
#     if y[i].isdigit():
#         print(y[i],end=" ")
#     elif y[i] in ("aeiou"):
#         print(y[i],end=" ")
#     i+=1


# x='one two three four five six'
# y=""
# i=0
# x=x.split()
# while i<=len(x):
#     if i%2==0:
#         y=x[i]
#     else:
#         y=x[i][::-1]
#     i+=1
# print(y)


# l=[1,2,3,4,5,6,7,8,9]
sum=0
# i=0
# l2=[]
# while i <= len(l)-1:
#     if l[i] % 2 == 0:
#         l2.append(l[i])
#          sum=sum+l[i]
#     i+=1
# print(l2)


# d={1:20,2:20,"b":"bat","a":"apple",4:60}
# d1=list(d.keys())
# print(d1)
# i=0
# while i<=len(d1)-1:
#     print(d1[i],end=" ")
#     i+=1

# s=["bat","ball",[1,2,3],{4,5},{90:87}]
# i=0
# while i<=len(s)-1:
#     if isinstance(s[i],dict):
#         print(s[i])
#     i+=1


#
# s1="good"
# s2="well"
# s3=" "




