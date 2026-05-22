class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def print_date(self):
        print (f"{self.day} / {self.month} / {self.year}")

date  = Date(24 , 'Sept', 2004)
date.print_date()

d1 = Date(23, 4, 2026)
print('D1  =',id(d1),d1.__dict__)

d2 = Date(24,4,2026)
print('D2 = ',id(d2),d2.__dict__)

d3 = Date(24,4,2026)
print('D3 = ',id(d3),d3.__dict__)

# d4 is object and in the d4 store the d3 address -- so both object of reference object is same
d4 = d2 
print('D4 =',id(d4),d4.__dict__)

