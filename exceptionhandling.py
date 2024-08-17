# l=[1,2,3,4]
# try:
#     l.replace(1,"Hello")   #AttributeError
#     print(l)
# except:
#      print("There is an Error")
#
#
# s=(23,45,67)
# try:
#     print(s.index(34))      #ValueError
# except ValueError:
#     print("Value is not present in the tuple")
#
#
# d={}
# try:
#     print(d.popitem()) #Key Error
# except KeyError:
#     print("There is no value in dictionary")
#
#
#
# k={1,2,3,4}
# try:
#     print(k.pop(23))
# except Exception as msg:
#     print(msg)


#Multiple Except Block
# a=[1,2,3,4,5,6]
# try:
#     print(a[3])
# except ZeroDivisionError:
#     print("exception is handeled")
# except ValueError:
#     print("exception is handeled")
# except AttributeError:
#     print("exception is handeled")
# except IndexError:
#     print("exception is handeled")
# finally:                                   #Finally is a keyword  #It will be executed if there is error or not
#     print("Finally Block is executed")



#Compression format
# try:
#     a[100]
# except(ZeroDivisionError,KeyError,AttributeError,ArithmeticError,IndexError):
#     print("\nException Is being handeled")
# finally:
#     print("No Error")



#Nested Try Block
# a=[1,2,3,4,5]
# try:
#     print(a[5])
#     try:
#        print(a[2])
#
#     except:
#         print("No is not Even")
# except:
#     print("Index Error")


# a="Hello"
# try:
#     print(a[4])
#     try:
#         if len(a)==3:
#             print(a[::-1])
#     except:
#         print("Len of String is not matching")
# except IndexError:
#     print("Error Occured")


# a="Akshay"
# try:
#     print(a[-5])
# except:
#     print("Error Occured")
# else:                               #If there is no error then it will only execute if there is an error it wont execute
#     print("Else block")
# finally:
#     print("Finally  Executed")



# class Metro_Error(Exception):
#     ...
# def check(a):
#     if a>0:
#         print("Posittive")
#     else:
#         raise Metro_Error
# check(10)
# check(-99)


# class Palindrome(Exception):
#     ...
# a=eval(input("Enter a String"))
# def palindrome(a):
#     if a==a[::-1]:
#         print("It is a Plaindrome")
#     else:
#         raise Palindrome
# palindrome(a)


