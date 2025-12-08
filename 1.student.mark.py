student_list = []
course_list = []

def add_student(name: str, id: str, DoB: str):
    s = {"Name": name,
         "ID": id,
         "Date of Birth": DoB}
    
    student_list.append(s)

def add_course(name: str, id: str):
    c = {"Name": name,
         "ID": id}
    
    course_list.append(c)
    
def display_student():
    for i in student_list:
        for l in i:
            print(f"Student {l}: {i[l]}")
            
def display_course():
    for i in course_list:
        for l in i:
            print(f"Course {l}: {i[l]}")

def add_score(sid: str, cid: str, mark):
    #if sid not in 
    pass

def main():
    add_student("Phạm Đức Anh","2410088","08/02/2006")
    display_student()
    
if __name__ == "__main__":
    main()