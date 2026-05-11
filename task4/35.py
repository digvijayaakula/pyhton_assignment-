a = list(map(int, input("enter numbers: ").split()))
b = a[0]
for c in a:
    if c > b:
        b = c
print(b)