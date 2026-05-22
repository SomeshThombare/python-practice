from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f'amount {amount} paid using card')

class UPIPaymtn(Payment):
    def pay(self,amount):
        print(f'amount {amount} paid using UPI')

class Netbanking(Payment):
    def pay(self, amount):
        print(f'amount {amount} paid using netbanking')


cp = CardPayment()
cp.pay(500)

upi = UPIPaymtn()
upi.pay(400)

nb = Netbanking()
nb.pay(300)

# payment = Payment()
# payment.pay(1000) --> u cant call abstract class