Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="WEL COME TO MY BLOG"
>>> 
>>> #come
>>> #+ve
>>> s[3:8]
' COME'
>>> s[4:8]
'COME'
>>> #-ve
>>> s[-12:-16:-1]
'EMOC'
>>> #+ve,-ve
>>> s[4:-11:1]
'COME'
#-ve,+ve
s[-12:4:-1]
'EMO'
s[-12:3:-1]
'EMOC'


#TO
#+ve
s[9:10]
'T'
s[9:11]
'TO'
#-ve
s[-9:-11:-1]
'OT'
#+ve,-ve
s[9:-8:1]
'TO'
#-ve,+ve
s[-9:-11:-1]
'OT'


#WEL
#+ve
s[0:3]
'WEL'
#-ve
s[-17::-1]
'LEW'
#+ve,-ve
s[0:-16:1]
'WEL'
#-ve,+ve
s[-17::-1]
'LEW'


#BLOG
#+ve
s[15::]
'BLOG'
#-ve
s[:-5:-1]
'GOLB'
#+ve.-ve
s[15::]
'BLOG'
#-ve,+ve
s[:14:-1]
'GOLB'


#CE
#+ve
s[4:8:2]
'CM'
s[4:8:3]
'CE'
#-ve
s[-11:-16:-3]
' O'
s[-12:-16:-3]
'EC'
#+ve,-ve
s[4:-11:3]
'CE'
#-ve,+ve
s[-12:3:-3]
'EC'



#WC
#+ve
s[:5:3]
'W '
s[:5:4]
'WC'
#-ve
s[-15::-4]
'CW'
#+ve,-ve
s[:-14:4]
'WC'
#-ve,+ve
s[-15::-4]
'CW'




x="be active in class"

#atv
#+ve
x[3:8:2]
'atv'
#-ve
x[-11:-16:-2]
'vta'
#+ve,-ve
x[3:-10:2]
'atv'
#-ve,+ve
x[-11:2:-2]
'vta'


#te
#+ve
x[5:9:3]
'te'
#-ve
x[-10:-14:-3]
'et'
#+ve,-ve
x[5:-9:3]
'te'
#-ve,+ve
x[-10:4:3]
''
x[-10:4:-3]
'et'


#lass
#+ve
x[14::]
'lass'
#-ve
x[:-5:-1]
'ssal'
#+ve,-ve
x[14::]
'lass'
#-ve,+ve
x[:13:-1]
'ssal'


#active
#+ve
x[3:9:]
'active'
#-ve
x[-10:-16:-1]
'evitca'
#+ve,-ve
x[3:-9]
'active'
#-ve,+ve
x[-10:2:-1]
'evitca'


