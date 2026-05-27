logs=[]
n=int(input("how many logs : "))

for i in range(n):
    logs.append(input("enter log : "))

count={}
unique=set()

for i in logs:
    data=i.split()
    level=data[0]
    unique.add(level)

    if level in count:
        count[level]=count[level]+1
    else:
        count[level]=1

print("log counts")
print(count)

print("unique log levels")
print(unique)