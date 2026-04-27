#assignment 7
n=int(input("enter n:"))
for i in range(1,n+1):
 print(i)

 
n=int(input("enter n:"))
s=0
for i in range(1,n+1):
 if i%2==0:
  s+=i
print("sum:",s)


n=int(input("enter number:"))
r=0
while n>0:
 d=n%10
 r=r*10+d
 n//=10
print("reverse:",r)
print("reverse:",r)


n=int(input("enter number:"))
c=0
while n>0:
 n//=10
 c+=1
print("digits:",c)


n=int(input("enter number:"))
for i in range(1,11):
 print(n,"*",i,"=",n*i)

 
n=int(input("enter size:"))
for i in range(n):
 for j in range(n):
  print("*",end=" ")
 print()

 
n=5
for i in range(1,n+1):
 print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1):
 print(" "*(n-i)+"*"*(2*i-1))


n=1
for i in range(4):
 for j in range(5):
  print(n,end=" ")
  n+=1
 print()

