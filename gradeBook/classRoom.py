from student import Student
import pdb
class Classroom():

    def __init__(self, className, date):
        self.next_student_ID = 0
        self. className = className
        self.date = date
        self.roster = {}


    # create a student object to roster +
    def create_student(self, student_name):
        # student_name = str(input("what's the name of the new student? "))
        # student_name = "mike"
        new_student = Student(student_name, self.next_student_ID)
        self.next_student_ID += 1
        self.roster[new_student.student_ID] = new_student
        # return self.roster


    def remove_student(self, student_name):
        key_to_be_deleted = None
        for k,v in self.roster.items():
            if v.studentName == student_name:
                key_to_be_deleted = k
        self.roster.pop(key_to_be_deleted, None)
        print(self.roster)

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
classroom1.create_student("sky")
classroom1.create_student("sky2")
# print(classroom1.roster)
classroom1.remove_student("sky")
print(classroom1.roster)
# print(classroom1.create_student("yo").student_ID)
# print(classroom1.create_student())

# print(classroom1.add_assignments())
# print(classroom1.get_average())



