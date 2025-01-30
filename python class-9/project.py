class fruit:
    def __init__(self,name):
        self.name = name   
        print("Constructor has been called")
        print("You created ", name)

f1 = fruit("apple")
print(f1.name)  

f1 = fruit("Banana")
print(f1.name)  

class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"This is a {self.year} {self.make} {self.model}.")
    
    def start(self):
        print(f"The {self.make} {self.model} is now starting.") 

car1 = car("Toyota", "Camry", 2022)
car2 = car("Honda", "Civic", 2021)

print(car1.description())
print(car2.description())

car1.start()
car2.start()

class Account:
    def __init__(self, balance , account_number):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs",amount,"from account",self.account_number,"credited successfully")
        print("Your current balance is Rs",self.balance)

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs",amount,"from account",self.account_number,"debited successfully")
        print("Your current balance is Rs",self.balance)

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1 = debit(5000)

acc2 = Account(1000, 12341235)
acc2 = credit(7000)