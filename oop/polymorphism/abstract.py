#Interface is a abstract class only but having all methods to type abstract.

from abc import ABC, abstractmethod
class RBI(ABC):

    @abstractmethod
    def account(self):
        pass

    @abstractmethod
    def rate_of_intrest(self):
        pass

class SBI(RBI):

    def account(self):
        print('700')

    def rate_of_intrest(self):
        print('7%')

class BOI(RBI):

    def account(self):
        print('800')

    def rate_of_intrest(self):
        print('8%')

sbi = SBI()
sbi.account()
sbi.rate_of_intrest()

boi = BOI()
boi.account()
boi.rate_of_intrest()

# rbi = RBI()
# rbi.account()
# rbi.rate_of_intrest()

'''typeError: Can't instantiate abstract class RBI without an implementation for abstract methods 'account', 'rate_of_intrest'''