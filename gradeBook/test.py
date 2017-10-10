import pytest
from student import Student
from classRoom import Classroom

def setup_test():
    classroom1 = Classroom("cs1","09/10")
    return classroom1

def test_setUp_classroom():
    classroom = setup_test()
    assert classroom.className == "cs1"
    assert classroom.date == "09/10"

def test_create_student():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    roster = classroom.create_student("sky2")
    assert roster[0].studentName == "sky"
    assert roster[0].student_ID == 0
    assert roster[1].studentName == "sky2"
    assert roster[1].student_ID == 1

def test_remove_student():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    classroom.remove_student("sky")
    assert classroom.roster == {}

def test_add_assignment():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    classroom.add_assignment("firstClass")
    assert classroom.roster[0].grades == {"firstClass":None}

def test_add_assignment_to_many():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    roster = classroom.create_student("sky2")
    classroom.add_assignment("firstClass")
    assert classroom.roster[0].grades == {"firstClass":None}
    assert classroom.roster[1].grades == {"firstClass":None}

def test_remove_assignment():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    classroom.add_assignment("firstClass")
    classroom.remove_assignment("firstClass")
    assert classroom.roster[0].grades == {}

def test_grade_student_assignment():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    classroom.add_assignment("firstClass")
    classroom.grade_student_assignment("firstClass", "sky")
    assert classroom.roster[0].grades == {'firstClass': 90}

def test_grade_manystudents_assignment():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    roster = classroom.create_student("sky2")
    classroom.add_assignment("firstClass")
    classroom.grade_student_assignment("firstClass", "sky")
    classroom.grade_student_assignment("firstClass", "sky2")
    assert classroom.roster[0].grades == {'firstClass': 90}
    assert classroom.roster[1].grades == {'firstClass': 90}



def test_get_average():
    classroom = setup_test()
    roster = classroom.create_student("sky")
    roster = classroom.create_student("sky2")
    classroom.add_assignment("firstClass")
    classroom.grade_student_assignment("firstClass", "sky")
    classroom.grade_student_assignment("firstClass", "sky2")
    classroom.get_average("firstClass")
    assert average == 90












