# Write your solution here
name = input("Whom should I sign this to:")
filename = input("Where shall I save it:")

with open(filename, 'w') as op_file:
    op_file.write(f"Hi {name}, we hope you enjoy learning Python with us! ")
    op_file.write("Best, Mooc.fi Team")