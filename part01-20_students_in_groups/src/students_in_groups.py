# Write your solution here
students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

no_of_groups = students//group_size

if (students > group_size*no_of_groups):
    no_of_groups+=1

print("Number of groups formed:", no_of_groups)