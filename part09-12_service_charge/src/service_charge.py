# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner:str, ac_no:str, balance:float):
        self.__owner = owner
        self.__ac_no = ac_no
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance:float):
        self.__balance = balance

    def __service_charge(self):
        self.__balance-=self.__balance*0.01

    def withdraw(self, amount:float):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")
        if amount >= self.__balance:
            raise ValueError("Insufficient balance to withdraw")
        self.__balance-=amount
        self.__service_charge()

    def deposit(self, amount:float):
        if amount <=0:
            raise ValueError("Invalid deposit amount")

        self.__balance+=amount
        self.__service_charge()

def main():
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

#main()