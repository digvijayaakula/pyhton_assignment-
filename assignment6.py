#assignment 6
#1
for i in range(1,11):
 print(i)

 #2
for i in range(1,51):
 if i%2==0:
  print(i)

  #3
n=int(input("enter number:"))
i=1
s=0
while i<=n:
 s+=i
 i+=1
print("sum:",s)

#4
n=int(input("enter number:"))
for i in range(1,11):
 print(n,"x",i,"=",n*i)

 #5
n=int(input("enter number:"))
c=0
while n>0:
 n//=10
 c+=1
print("digits:",c)

#6
n=int(input("enter number:"))
r=0
while n>0:
 d=n%10
 r=r*10+d
 n//=10
print("reverse:",r)

#7
for i in range(1,6):
 for j in range(i):
  print("*",end=" ")
 print()

 #8
n=int(input("enter number:"))
f=0
for i in range(2,n):
 if n%i==0:
  f=1
  break
if n>1 and f==0:
 print("prime")
else:
 print("not prime")

 #9
for i in range(1,11):
 if i==5:
  continue
 if i==9:
  break
 print(i)

 #10
n=int(input("enter number:"))
f=1
for i in range(1,n+1):
 f*=i
print("factorial:",f)

