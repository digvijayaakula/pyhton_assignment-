a = int(input("enter number: "))
b = 0
while a > 0:
    c = a % 10
    b = b + c
    a = a // 10
print(b)