marks = input("Enter marks: ").split()
marks = list(map(int, marks))
passed = list(filter(lambda x: x >= 50, marks))
print(passed)