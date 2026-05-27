from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay(self,amount):
        print("credit card payment done :",amount)

class UPIPayment(Payment):
    def pay(self,amount):
        print("upi payment done :",amount)

choice=input("enter payment method (card/upi) : ")
amount=int(input("enter amount : "))

if choice=="card":
    obj=CreditCardPayment()
elif choice=="upi":
    obj=UPIPayment()
else:
    obj=None

if obj!=None:
    obj.pay(amount)
else:
    print("invalid method")