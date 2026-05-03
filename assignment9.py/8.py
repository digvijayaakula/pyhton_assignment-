numbers = input("Enter numbers: ").split()
numbers = list(map(int, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)