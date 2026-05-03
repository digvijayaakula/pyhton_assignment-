from functools import reduce
numbers = input("Enter numbers: ").split()
numbers = list(map(int, numbers))
total = reduce(lambda x, y: x + y, numbers)
print(total)