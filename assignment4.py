#assignment4
#1
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("modulus:",a%b)
print("exponent:",a**b)
print("floor division:",a//b)

#2
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("a>b:",a>b)
print("a<b:",a<b)
print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)

#3
a=True
b=False
print("a and b:",a and b)
print("a or b:",a or b)
print("not a:",not a)

#4
num=int(input("enter a number:"))
if num>=10 and num<=50:
 print("number is between 10 and 50")
else:
 print("number is not between 10 and 50")

#5
x=10
print("initial:",x)
x+=5
print("after+=5:",x)
x-=3
print("after-=3:",x)
x*=2
print("after*=2:",x)
x/=4
print("after/=4:",x)

#6
lst=[10,20,30,40,50]
value=int(input("enter value:"))
if value in lst:
 print("value exists")
else:
 print("value does not exist")

#7
a=[1,2,3]
b=[1,2,3]
c=a
print("a==b:",a==b)
print("a is b:",a is b)
print("a==c:",a==c)
print("a is c:",a is c)

#8
num=int(input("enter a number:"))
if num%2==0:
 print("even")
else:
 print("odd")

#9
l=float(input("enter length:"))
b=float(input("enter breadth:"))
area=l*b
print("area:",area)

#10
r1=10+5*2
r2=(10+5)*2
print("without parentheses:",r1)
print("with parentheses:",r2)
