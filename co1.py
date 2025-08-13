class Bankaccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self):
        amount=int(input("Enter the amount to be deposited:"))
        self.balance+=amount
        print(f"The balance of {self.owner}is {self.balance}")
    
    def withdraw(self):
        w_amount=int(input("Enter the amount to be withdraawn:"))
        if (w_amount<=self.balance):
            self.balance-=w_amount
            print(f"The amount balance left after withdrawing{w_amount} is{self.balance}")
        else:
            print("insufficient balance")
            
    def display_balance(self):
        print(f"The current balance of {self.owner} is {self.balance}")
        
Account1=Bankaccount("Ambani",20000)
Account2=Bankaccount("Adani",10000)
Account3=Bankaccount("Rahul")

Account1.display_balance()
Account2.display_balance()
Account3.display_balance()

Account1.deposit()
Account2.deposit()
Account3.deposit()

Account1.withdraw()
Account2.withdraw()
Account3.withdraw() 