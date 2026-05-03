salaries = input("Enter salaries: ").split()
salaries = list(map(int, salaries))
high = list(filter(lambda x: x > 50000, salaries))
print(high)