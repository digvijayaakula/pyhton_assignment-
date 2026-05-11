a = int(input("enter start: "))
b = int(input("enter end: "))
for c in range(a, b + 1):
    if c > 1:
        d = 0
        for e in range(1, c + 1):
            if c % e == 0:
                d = d + 1
        if d == 2:
            print(c, end=" ")
print()