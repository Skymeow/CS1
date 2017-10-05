import math
class Student():
    id = 0
    def __init__(self, studentName):
        self.studentName = studentName
        Student.id += 1
        self.student_ID = id
        self.grade = None
        self.grades = {}

    # def student_name_dict(self):
    #     roster_dict = {}
    #     roster_dict[self.id] = self
    #     return(roster_dict)

# roster = {}
# for number in range(2):
#     new_student = Student()
#     roster.append(new_student)
#     print(roster)

    # create a list of student object
    # def add_student(studentName, add_id):
    #     print(student)

# have a encupsulated dictionary under each student object
# {assignmentname: grade}
    # def grade_assignment(self):
    #     # call the assignment method in classroom to get the list of assignment
    #     assignments = ["cs1", "cs2"]
    #     for i in assignments:
    #         grade = int(input("what's the grade for this assignment? "))
    #         self.grades[i] =  grade
    #         print(self.grades)
    #         if len(self.grades) == len(assignments):
    #             break

    def grade_assignment(self, assignment_name, grade):
        self.grades[assignment_name] = grade

    #first get a grade from one student of the assignment, call in classromm see all student's grades for one assignment
    def get_grade_for_assignment(self, assignment_name):
        return self.grades[assignment_name]

# add/move more assignment in student class
# add a dic for assignments and give it's grade value of None first? change the grade in grade_assignment?
    def add_assignment(self, assignment_name):
        self.grades[assignment_name] = None

    def remove_assignment(self, assignment_name):
        # return my_dict[key] if key exists in the dictionary, and None otherwise.
        self.grades.pop(assignment_name, None)

# a func to add all grades of the student
    def all_assignments_grades(self):
        sum_grades = sum(self.grades.values())
        return sum_grades




# sky = Student("sky")
# print(sky.id)
# sky.grade_assignment("hw1", 100)
# sky.grade_assignment("hw2", 200)
# print(sky.student_name_dict())
# print(sky.get_grade_for_assignment('hw2'))

