# Write your solution here
def validate_header(header:str):
    parts = header.split(" ")
    try:
        week_no = int(parts[1])
        return True
    except ValueError:
        #print("Incorrect week no")
        return False

def validate_numbers(numbers:str):
    #print(numbers)
    parts = numbers.split(",")

    if len(parts) < 7:
        return False
    
    valid = True

    for num in parts:
        #print(num)
        try:
            int_num = int(num)
        except ValueError:
            return False
        
        if int_num <1 or int_num > 39:
            return False
        
        first_index = parts.index(num)
        try:
            second_index = parts[first_index+1:].index(num)
            return False
        except ValueError:
            pass 

    return valid

def filter_incorrect():
    ip_file = 'lottery_numbers.csv'
    op_file = 'correct_numbers.csv'

    op_list = []

    with open(ip_file) as ip_file:
        for line in ip_file:
            header_delim_index = line.find(";")
            if header_delim_index == -1:
                continue
            header = line[:header_delim_index]
            numbers = line[header_delim_index+1:].strip()
            if validate_header(header) and validate_numbers(numbers):
                op_list.append(line)
        
    with open(op_file,'w') as op_file:
        for row in op_list:
            op_file.write(row)



#filter_incorrect()