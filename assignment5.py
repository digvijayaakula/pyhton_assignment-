#assignment 5
#1
import string


s=input("enter string:")
print("uppercase:",s.upper())
print("lowercase:",s.lower())

#2
s=input("enter string:")
v="aeiou"
c=0
for i in s.lower():
 if i in v:
  c+=1
print("vowels:",c)

#3
s=input("enter string:")
print(s.replace(" ","-"))

#4
s=input("enter string:")
c=0
for i in s:
 c+=1
print("length:",c)

#5
s=input("enter string:")
if s==s[::-1]:
 print("palindrome")
else:
 print("not palindrome")

#6
s=input("enter sentence:")
w=s.split()
print("words:",len(w))

#7
s=input("enter string:")
ch=input("enter character:")
print("count:",s.count(ch))

#8
s=input("enter string:")
print(s.strip())

#9
s=input("enter string:")
if s.isdigit():
 print("only digits")
else:
 print("not only digits")

#10
s=input("enter string:")
if s.isdigit():
 print("only digits")