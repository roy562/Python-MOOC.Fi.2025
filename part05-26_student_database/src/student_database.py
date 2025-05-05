# Write your solution here
def add_student(students:dict, name:str):
    students[name] = None

def print_student(students:dict, name:str):
    if name in students:
        print(f"{name}:")
        if students[name] == None:
            print(" no completed courses")
        else:
            total_courses = len(students[name])
            print(f" {total_courses} completed courses:")
            course_sum = 0
            for course in students[name]:
                course_name, course_grade = course
                print(f"  {course_name} {course_grade}")
                course_sum+=course_grade
            print(f" average grade {course_sum/total_courses}")
    else:
        print(f"{name}: no such person in the database")

def add_course(students:dict, name:str, course:tuple):
    temp_list = []
    if (course[1] == 0) or (name not in students):
        return
    
    if students[name] != None:
        course_exists = False
        for rec_course in students[name]:
            if rec_course[0] == course[0]:
                course_exists = True
                if rec_course[1] < course[1]:
                    students[name].remove(rec_course)
                    students[name].append(course)
        if course_exists == False:
            students[name].append(course)
    else:
        temp_list.append(course)
        students[name] = temp_list
    
    #print(students)

def course_summary(student_courses:list):
    no_of_courses = len(student_courses)
    course_sum = 0
    for course in student_courses:
        course_sum+= course[1]
    grade_avg = course_sum/no_of_courses

    return no_of_courses,grade_avg

def summary(students:dict):
    print(f"students {len(students)}")
    course_stats = []
    stats_tuple = ()
    for key,value in students.items():
        no_of_courses, grade_avg = course_summary(value)
        stats_tuple = (key, no_of_courses, grade_avg)
        course_stats.append(stats_tuple)
    
    max_courses = course_stats[0]
    max_avg = course_stats[0]

    for item in course_stats:
        if item[1] > max_courses[1]:
            max_courses = item
        if item[2] > max_avg[2]:
            max_avg = item
    
    print(f"most courses completed {max_courses[1]} {max_courses[0]}")
    print(f"best average grade {max_avg[2]} {max_avg[0]}")

    
    


if __name__ == "__main__":
    students = {}
    
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")
    #add_student(students, "Peter")
    #add_student(students, "Eliza")
    #add_course(students, "Peter", ("Introduction to Programming", 3))
    #add_course(students, "Peter", ("Advanced Course in Programming", 2))
    #add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    #add_course(students, "Peter", ("Introduction to Programming", 2))
    #print_student(students, "Peter")
    #print_student(students, "Eliza")
    #print_student(students, "Jack")
    #add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    #add_course(students, "Peter", ("Introduction to Programming", 1))
    #add_course(students, "Peter", ("Advanced Course in Programming", 1))
    #add_course(students, "Eliza", ("Introduction to Programming", 5))
    #add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    #print_student(students, "Eliza")
    #print_student(students, "Peter")
    #summary(students)