# Write your solution here
def formatted(ip_list):
    new_list=[]
    for num in ip_list:
        new_list.append(f"{num:.2f}")
    
    return new_list
