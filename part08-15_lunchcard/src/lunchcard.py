# Write your solution here:
class LunchCard():
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        meal_cost = 2.6
        if self.validate_balance(meal_cost):
            self.balance-=meal_cost
    
    def eat_special(self):
        meal_cost = 4.6
        if self.validate_balance(meal_cost):
            self.balance-=meal_cost
    
    
    def validate_balance(self, meal_cost:float):
        return (self.balance-meal_cost) > 0

    def deposit_money(self, deposit:float):
        if deposit < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        
        self.balance+=deposit

def main():
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)
    peters_card.eat_special()
    graces_card.eat_lunch()
    print("Peter: "+str(peters_card))
    print("Grace: "+str(graces_card))
    peters_card.deposit_money(20)
    graces_card.eat_special()
    print("Peter: "+str(peters_card))
    print("Grace: "+str(graces_card))
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    graces_card.deposit_money(50)
    print("Peter: "+str(peters_card))
    print("Grace: "+str(graces_card))

main()