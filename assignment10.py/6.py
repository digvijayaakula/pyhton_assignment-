def calculate_price(price,tax=5,discount=0):
    return price+(price*tax/100)-discount

price=int(input("enter price : "))
tax=int(input("enter tax % : "))
discount=int(input("enter discount : "))

print("final price :",calculate_price(price,tax,discount))