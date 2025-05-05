# Write your solution here
gift = int(input("Value of gift:"))

gift_tax = 0.0

if gift >=5000 and gift <25000:
    gift_tax = 100+(gift-5000)*0.08
elif gift >=25000 and gift <55000:
    gift_tax = 1700+(gift-25000)*0.1
elif gift >=55000 and gift <200000:
    gift_tax = 4700+(gift-55000)*0.12
elif gift >=200000 and gift <1000000:
    gift_tax = 22100+(gift-200000)*0.15
elif gift >=1000000:
    gift_tax = 142100+(gift-1000000)*0.17

if gift_tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {gift_tax} euros")