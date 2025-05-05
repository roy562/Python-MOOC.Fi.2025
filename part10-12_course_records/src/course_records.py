# tee ratkaisusi tänne
class CourseBook:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, course_name:str, grade:int, credits:int):
        if course_name not in self.__courses:
            self.__courses[course_name] = (grade, credits)
        else:
            course_grcr = self.__courses[course_name]
            if grade > course_grcr[0]:
                self.__courses[course_name] = (grade, credits)
        #print(self.__courses)
    
    def get_course(self, course_name:str):
        if course_name not in self.__courses:
            print("no entry for this course")
        else:
            grcr = self.__courses[course_name]
            print(f"{course_name} ({grcr[1]} cr) grade {grcr[0]}")
    
    def get_stats(self):
        course_count = len(self.__courses)
        credit_sum = 0
        grade_sum = 0
        grade_dist = {}
        for grcr in self.__courses.values():
            credit_sum+= grcr[1]
            grade_sum+=grcr[0]
            grade = grcr[0]
            if grade not in grade_dist:
                grade_dist[grade] = 0
            grade_dist[grade]+=1
        
        print(f"{course_count} completed courses, a total of {credit_sum} credits")
        print(f"mean {round(grade_sum/course_count,1)}")
        print("grade distribution")
        for i in range(5, 0, -1):
            grade_count = grade_dist[i] if i in grade_dist.keys() else 0
            print(f"{i}: {grade_count*'x'}")


class StudiesApplication():
    def __init__(self):
        self.__coursebook= CourseBook()
    
    def __initialize(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        print()

    def __add_course(self):
        course_name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__coursebook.add_course(course_name, grade, credits)
    
    def __get_course(self):
        course_name = input("course: ")
        self.__coursebook.get_course(course_name)

    def __get_statistics(self):
        self.__coursebook.get_stats()

    def execute(self):
        self.__initialize()
        while True:
            print()
            try:
                user_option = int(input("command: "))
            except:
                continue
            if user_option == 0:
                break
            elif user_option == 1:
                self.__add_course()
                
            elif user_option == 2:
                self.__get_course()
            elif user_option == 3:
                self.__get_statistics()
            else:
                print("Invalid option")
                break




studies = StudiesApplication()
studies.execute()

#{'ItP': (5, 5), 'ACiP': (1, 10), 'ItAI': (2, 5), 'Algo101': (4, 1), 'CompModels': (5, 8)}