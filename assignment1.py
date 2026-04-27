#1. Program to Calculate the Area of a Circle

pi=3.14159265359
r=float(input("enter radius of circle = "))
a=pi*r**2
print("area of circle = ",a)

# 2. Program to Calculate Total Cost After Discount

op=int(input("enter original price = "))
dp=int(input("enter discount percentage = "))
sp=op-((dp/100)*op)
print("selling price = ",sp)

# 3. Program to Calculate Simple Interest

p=int(input("enter principal amount ="))
r=float(input("enter rate of intrest ="))
t=float(input("enter time ="))
si = (p*t*r)/100
print ("simple intrest is =",si)

# 4. Program to Calculate Total Salary

print("Hi Employee")
bs=int(input("enter your basic salary = "))
hrs=int(input("enter your house rent allowance = "))
da=int(input("enter your dearness allowance = "))
ts=bs+hrs+da
print("your total salary = ",ts)

# 5. Program to Calculate Distance Traveled

s=float(input("enter speed of the vehicle = "))
t=float(input("enter time traveling by vehicle = "))
d=s*t
print("distance traveled by vehicle = ",d)

# 6. Program to Convert Temperature from Celsius to Fahrenheit

c = float(input("enter celsius: "))
f = (c * 9/5) + 32
print("fahrenheit =", f)
a= int(input("enter a value = "))
b=int(input("enter b value = "))
if a>b:
    print("max value is  = ",a)
else:
    print("max value is = ",b)

#7 .Program to Find the Maximum of Two Numbers Using Ternary Operator

a= int(input("enter a value = "))
b=int(input("enter b value = "))
if a>b:
    print("max value is  = ",a)
else:
    print("max value is = ",b)

# 8. Swap Two Numbers

a=int(input("enter a value = "))
b=int(input("enter b value = "))
a,b=b,a
print("a = ",a)
print("b = ",b)

#9. Next Multiple of 100

n = int(input("Enter a number: "))
next_multiple = (n // 100 + 1) * 100
print(next_multiple)

#10. Splitting into the Teams

people = int(input("Enter number of people: "))
teams = people // 2
left = people % 2
print("Teams formed:", teams)
print("People left without a team:", left)