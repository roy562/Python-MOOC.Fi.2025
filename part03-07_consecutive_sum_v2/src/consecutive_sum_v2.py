# Write your solution here

# Write your solution here
limit = int(input("Limit:"))
number = 1
total=0
o_string = f"The consecutive sum: "

while total < limit:
    total+=number
    if number == 1:
        o_string+=f"{number}"
    else:
        o_string+=f" + {number}"
    number+=1

o_string+=f" = {total}"
print(o_string)