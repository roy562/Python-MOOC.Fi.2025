from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts:list):
    return reduce(lambda r_sum, course: r_sum+course.credits, attempts, 0)

def sum_of_passed_credits(attempts:list):
    passed_attempts = filter(lambda att: att.grade > 0 , attempts)
    return reduce(lambda p_credit, att: p_credit+att.credits, passed_attempts, 0)

def average(attempts:list):
    passed_attempts = list(filter(lambda att: att.grade > 0 , attempts))
    grade_total = reduce(lambda p_grade, att: p_grade+att.grade, passed_attempts, 0)
    return grade_total/len(passed_attempts)

def test1():
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

#test1()

def test2():
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

#test2()

def test3():
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)

#test3()