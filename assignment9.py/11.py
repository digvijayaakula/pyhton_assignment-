from functools import reduce
numbers = input("Enter numbers: ").split()
numbers = list(map(int, numbers))
product = reduce(lambda x, y: x * y, numbers)
print(product)