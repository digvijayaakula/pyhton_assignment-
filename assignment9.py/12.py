prices = input("Enter prices: ").split()
prices = list(map(int, prices))
discounted = list(map(lambda x: x * 0.9, prices))
print(discounted)