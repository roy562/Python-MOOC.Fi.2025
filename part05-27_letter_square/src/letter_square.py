# Write your solution here
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def create_square(layers:int):
    op_list = [['A']]
    current_layer = 1

    if layers==1:
        return op_list
    
    while current_layer<layers:
        for row in op_list:
            row.insert(0,alphabets[current_layer])
            row.append(alphabets[current_layer])
        op_list.insert(0,[alphabets[current_layer]]*len(row))
        op_list.append([alphabets[current_layer]]*len(row))
        current_layer+=1
    
    return op_list

def print_square(square_list:list):
    for line in square_list:
        print(''.join(line))

def main():
    layers = int(input("Layers:"))
    op_list = create_square(layers)
    print_square(op_list)

main()

