numbers = input("Enter numbers: ").split()
numbers = list(map(int, numbers))
squares = list(map(lambda x: x * x, numbers))
print(squares)