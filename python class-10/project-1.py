class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"hello,{self.name}! you age is {self.age}")
    
    def greeting(self):
        print(f"Welcome,{self.name}! have great day!")

    def __del__(self):
        print(f"Goodbye,{self.name}! have a nice day!")

print("Creating a person object")
person1 = person("Izyan", 16)

print("Calling the greet method")
person1.greet()

print("Deleting the person object")
del person1

class bank_account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        print(f"Account created for {self.name} with account number {self.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited into account successfully. Current balance : {self.balance}")
        else:
            print("Invalid deposit amount.")

        def withdraw(self, amount):
            if 0 > amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn from account successfully.Current balance : {self.balance}")
            else:
                print("Invalid withdrawal amount or insufficient balance.")

        def __del__(self):
            print(f"Account deleted for {self.name} with account number {self.account_number}")


