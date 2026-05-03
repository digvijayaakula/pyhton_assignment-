a = int(input("enter balance: "))
b = int(input("enter withdraw amount: "))
if b <= a:
    print("transaction successful")
else:
    print("insufficient balance")