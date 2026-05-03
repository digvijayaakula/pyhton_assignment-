#2.

def big(list1):
    big = list1[0]
    for n in list1:
        if n > big:
            big = n
    return big

def small(list1):
    small = list1[0]
    for n in list1:
        if n < small:
            small = n
    return small

def add_all(list1):
    total = 0
    for n in list1:
        total += n
    return total

num1 = [4, 8, 1, 9]
print("Maximum:", big(num1))
print("Minimum:", small(num1))
print("Sum:", add_all(num1))

num2 = [-5, -2, -10]
print("Maximum:", big(num2))
print("Minimum:", small(num2))
print("Sum:", add_all(num2))
