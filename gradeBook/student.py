
class Student():
    id = 0
    def __init__(self, studentName):
        self.studentName = studentName
        Student.id += 1
        self.grade = None
        self.grades = {}

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

    def get_grade_for_assignment(self, assignment_name):
        return self.grades[assignment_name]


# sky = Student("sky")
# sky.grade_assignment("hw1", 100)
# sky.grade_assignment("hw2", 200)
# print(sky.get_grade_for_assignment('hw2'))
