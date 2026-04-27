#assignment3

'''
students = ["Amit", "Ravi", "Sita", "Neha", "Kiran"]
students.append("vijay")
students.remove("Ravi")
print(students)
'''
'''
numbers = [12, 45, 7, 23, 89, 2]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest:", largest)
print("Smallest:", smallest)
'''

'''
t = (10, "hello", 3.5, True)
print(t[0])
print(t[1])
l = list(t)
l[0] = 20
t = tuple(l)
print(t)
'''

'''
numbers = [1, 2, 3, 2, 4, 1, 5]
numbers = list(set(numbers))
print(numbers)
'''

'''
emp={"id":101,"name":"John","salary":50000}
emp["department"]="IT"
emp["salary"]=60000
del emp["name"]
print(emp)
'''

'''
emp={"id":101,"name":"John","salary":50000}
for k in emp:
    print(k)
for v in emp.values():
    print(v)
for k,v in emp.items():
    print(k,v)
'''

'''
a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(a&b)
print(a-b)
'''

'''
l=[1,2,2,3,3,3,4]
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''

'''
l=["milk","bread","eggs"]
t=("red","blue","green")
s={101,102,103,103}
d={"name":"John","age":20}

print(l)
print(t)
print(s)
print(d)
'''

'''
l=[10,20,30]
l.append(40)
print(l)
t=(10,20,30)
print(t)
s={1,2,3}
s.add(4)
print(s)
d={"id":1,"name":"Asha"}
d["age"]=21
print(d)
'''