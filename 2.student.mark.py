class Thing:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class Student(Thing,):
    def __init__(self,name,id,DoB):
        super().__init__(name,id)
        self.DoB = DoB
        
class List:
    def __init__(self):
        self.list = []
        self.count = 0
        self.number = int(input())
        
    def add(self):
        pass
    
    def display(self):
        pass
        
class CourseList(List):
    def add(self):
        name = input("Course name: ")
        id = input("Course ID: ")
        
        subject = Thing(name,id)
        
        self.list.append(subject)
        self.count += 1
        
    def display(self):
        for i in range(self.count):
            print(f"Course {i}:")
            print(f"Name: {self.list[i].name}")
            print(f"ID: {self.list[i].id}")
            
        
class StudentList(List):
    def add(self):
        name = input("Student name: ")
        id = input("Student ID: ")
        DoB = input("Student date of birth: ")
        
        student = Student(name,id,DoB)
        
        self.list.append(student)
        self.count += 1
        
    def display(self):
        for i in range(self.count):
            print(f"Student {i + 1}:")
            print(f"Name: {self.list[i].name}")
            print(f"ID: {self.list[i].id}")
            print(f"Date of Birth: {self.list[i].DoB}")
            
list = StudentList()
for i in range(3):
    list.add()
list.display()