from main import StudentsInMLOps

def test_enrollStudents():
    student_manager = StudentsInMLOps()
    student_manager.enrollStudents(5)
    assert student_manager.getTotalStrength() == 5

def test_dropStudents():
    student_manager = StudentsInMLOps()
    student_manager.enrollStudents(10)
    student_manager.dropStudents(3)
    assert student_manager.getTotalStrength() == 7