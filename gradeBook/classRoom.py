from student import Student
import pdb
class Classroom():

    def __init__(self, className, date):
        self.next_student_ID = 0
        self.className = className
        self.date = date
        self.roster = {}


    # + create a student object to roster
    def create_student(self, student_name):
        # student_name = str(input("what's the name of the new student? "))
        # student_name = "mike"
        new_student = Student(student_name, self.next_student_ID)
        self.next_student_ID += 1
        self.roster[new_student.student_ID] = new_student
        return self.roster

# +
    def remove_student(self, student_name):
        key_to_be_deleted = None
        for k,v in self.roster.items():
            if v.studentName == student_name:
                key_to_be_deleted = k
        self.roster.pop(key_to_be_deleted, None)
        return self.roster

# get all averge of the rooster within the classroom
    def get_average(self, single_assignment):
        students_collection = list(self.roster.values())
        print(students_collection)
        num_student = len(students_collection)
        single_assignment = "firstClass"
        # single_assignment = input("which assignment do you wanna see the average? ")
        scores = 0
        for i in students_collection:
            print(i.studentName)
            score = int(i.grades[single_assignment])
            print(score)
            scores += score
            print(scores, num_student)
            average = scores/num_student
        return average


    # + have teachers to add an assignment to all students in the classroom,call student.garde_assignment?
    # give grade actually value when grade it
    def add_assignment(self, assignment_name):
        for f,v in self.roster.items():
            grade = None
            v.grade_assignment(assignment_name, grade)
        return v.grades

    # + teacher give each student different grades
    def grade_student_assignment(self, assignment_name, student_name):
        for f, v in self.roster.items():
            if v.studentName == student_name:
                grade = 90
                # grade = input("what's the grade for " + v.studentName)
                v.grade_assignment(assignment_name, grade)
                return v.grades
            else:
                print('not the same student you wanna grade')
                # grade = input("what's the grade for "+v.studentName)
                # v.grade_assignment(assignment_name, grade)



# + remove assignment from all roster in the classroom
    def remove_assignment(self, assignment_name):
        for f,v in self.roster.items():
            v.grades.pop(assignment_name, None)
            print(v.grades)

# classroom1 = Classroom("cs1","09/10")
# classroom1.create_student("sky")
# classroom1.create_student("sky2")
# # print(classroom1.roster)
# # classroom1.remove_student("sky")
# # print(classroom1.roster)
# # print(classroom1.create_student("yo").student_ID)
# # print(classroom1.create_student())

# # print(classroom1.add_assignments())
# classroom1.add_assignment("mysteryassignment")
# classroom1.grade_student_assignment("mysteryassignment", "sky")
# classroom1.grade_student_assignment("mysteryassignment", "sky2")
# print(classroom1.roster[1].grades)
# # print(classroom1.Student("sky").grade_assignments("mysteryassignment",100))

# print(classroom1.get_average())



