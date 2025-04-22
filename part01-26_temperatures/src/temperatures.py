# Write your solution here
tempF = int(input("Please type in a temperature(F): "))

tempC = (tempF-32)/1.8

print(f"{tempF} degrees Fahrenheit equals {tempC} degrees Celsius")

if tempC < 0:
    print("Brr! It's cold in here!")