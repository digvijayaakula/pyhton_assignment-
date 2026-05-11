a = input("enter string: ")
b = 0
for c in a:
    if c in "aeiouAEIOU":
        b = b + 1
print(b)