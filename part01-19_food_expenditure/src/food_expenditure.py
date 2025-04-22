# Write your solution here
meals_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print("Daily:",(meals_per_week*price+groceries)/7,"euros")
print("Weekly:",meals_per_week*price+groceries,"euros")