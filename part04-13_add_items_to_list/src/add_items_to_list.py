# Write your solution here
no_of_items = int(input("How many items:"))
my_list = []
i=1

while i <= no_of_items:
    item = int(input(f"Item {i}:"))
    my_list.append(item)
    i+=1

print(my_list) 