class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student_object):
        self.students.append(student_object)


if __name__ == "__main__":
    course = Course("Intro to Python")
    
    s1 = Student("Thirdskee", "6767")
    s2 = Student("PisayKila", "6969")
    
    course.add_student(s1)
    course.add_student(s2)
    
    print(f"Course Name: {course.course_name}")
    print("Students enrolled:")
    for student in course.students:
        print(f"- {student.name} ({student.student_id})")
