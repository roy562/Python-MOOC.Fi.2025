# Write your solution here:
def sort_by_remaining_stock(items: list):

    def sort_by_stock(item:tuple):
        return item[2]
    
    sorted_items = sorted(items, key=sort_by_stock)
    return sorted_items

def test():
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")

#test()