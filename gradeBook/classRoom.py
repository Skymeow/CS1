from student import Student
class Classroom():

    def __init__(self, className, date):
        self. className = className
        self.date = date
        self.roster = {}


    # create a student object to roster
    def create_student(self):
        student_name = str(input("what's the name of the new student? "))
        new_student = Student(student_name)
        self.roster.update(new_student)
        print(self.roster)

    # create a list assignments
    def add_assignments():
        assignment = input("what's the assignment? ")
        assignments = []
        assignments.append(assignment)
        return(assignments)



classroom1 = Classroom("cs1","09/10")
print(classroom1.create_student())
# print(classroom1.add_assignments())




