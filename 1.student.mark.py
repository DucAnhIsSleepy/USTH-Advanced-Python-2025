student_list = []
course_list = []

def add_student():
    student = []
    
    ID = input("Input ID: ")
    Name = input("Input name: ")
    DoB = input("Input date of birth: ")
    
    student.append(ID)
    student.append(Name)
    student.append(DoB)
    
    student_list.append(student)

def add_course():
    course = []
    
    ID = input("Input ID: ")
    Name = input("Input name: ")
    
    course.append(ID)
    course.append(Name)
    
    course_list.append(course)

me = {
    "name" : "Duc Anh",
    "BoD" : "08/02/2006"
}