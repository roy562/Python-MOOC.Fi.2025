class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    return list(filter(lambda a:a.grade>=1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda a: a.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    passed = list(filter(lambda a: a.grade > 0 and a.course_name == course, attempts))
    return sorted(list(map(lambda p: p.student_name, passed)))

def test1():
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

    for attempt in accepted([s1, s2, s3]):
        print(attempt)

#test1()

def test2():
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)

#test2()

def test3():
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)

#test3()