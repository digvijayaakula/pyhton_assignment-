a = int(input("enter number: "))
b = 0
if a == 0:
    b = 1
else:
    while a > 0:
        a = a // 10
        b = b + 1
print(b)