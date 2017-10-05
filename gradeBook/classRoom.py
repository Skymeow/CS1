from student import Student
import pdb
class Classroom():

    def __init__(self, className, date):
        self. className = className
        self.date = date
        self.roster = {}


    # create a student object to roster
    def create_student(self, student_name):
        # student_name = str(input("what's the name of the new student? "))
        # student_name = "mike"
        new_student = Student(student_name)
        self.roster[new_student.student_ID] = new_student
        return self.roster


    def remove_student(self):
        # ask the teacher to isnput the id of student she wants to delete
        id = int(input("what's the Id of the student you wanna delete? "))
        self.roster.pop(id, None)
        return(self.roster)
    # create a list assignments
    def add_assignments():
        assignment = input("what's the assignment? ")
        assignments = []
        assignments.append(assignment)
        return(assignments)


    def get_average(self):
        students_collection = self.rooster.values()
        num_student = len(students_collection)
        single_assignment = str(input("which assignment do you wanna see the average? "))
        scores = 0
        for i in students_collection:
            score = i.get_grade_for_assignment(single_assignment)
            scores += score
            average = scores/num_student
            return average




classroom1 = Classroom("cs1","09/10")
added_roster = classroom1.create_student("sky")

# print(classroom1.create_student("yo").student_ID)
# print(classroom1.create_student())

# print(classroom1.add_assignments())
# print(classroom1.get_average())



