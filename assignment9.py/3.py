def apply_operation(func, a, b):
    return func(a, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter + or *: ")
if op == "+":
    print(apply_operation(lambda x, y: x + y, a, b))
else:
    print(apply_operation(lambda x, y: x * y, a, b))