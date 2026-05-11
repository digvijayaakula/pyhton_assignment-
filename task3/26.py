a = int(input("enter number: "))
b = 0
for c in range(1, a + 1):
    if a % c == 0:
        b = b + 1
if b == 2:
    print("prime")
else:
    print("not prime")