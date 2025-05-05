# Write your solution here
my_list=[]
my_list_sorted=[]

while True:
    new_item = int(input("New item:"))

    if new_item == 0:
        print("Bye!")
        break
    else:
        my_list.append(new_item)
        print("The list now:", my_list)
        my_list_sorted=sorted(my_list)
        print("The list in order:", my_list_sorted)

