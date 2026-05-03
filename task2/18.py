a = int(input("enter amount: "))
if a > 1000:
    print("10% discount")
elif a >= 500:
    print("5% discount")
else:
    print("no discount")