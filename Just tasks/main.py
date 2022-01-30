import json

def getLogin(name, password):

    with open('db_users.json', 'r') as f:
        info = json.load(f)
        for key in info:
            if key == name and info[key]["password"] == password:
                return True
            
    return False

def getItemRole(name):
    with open('db_users.json', 'r') as f:
        info = json.load(f)
        for key in info:
            if key == name:
                return info[key]["role"]
    return "none"

class Course:
    def __init__(self, name, grade, attendance, free):
        self.name = name
        self.free = free
        self.grade = grade
        self.attendance = attendance

def pointsToGPA(points):
    return points/23
def gpaToLetter(gpa):
    if gpa > 3:
        return 'A'
    if gpa > 2:
        return 'B'
    if gpa > 1:
        return 'C'
    if gpa > 0:
        return 'D'
    else:
        return 'F'
class Student:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def showGrades(self):

        ans = ""
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for i in range(0, len(info[self.name]["cource_list"])):
                    ans += str(info[self.name]["cource_list"][i]["grade"]) + " "
            except:
                print("No subscription to cources")
        return ans

    def showAvgGPA(self):
        ans = 0.0
        credit = 0.0
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for i in range(0, len(info[self.name]["cource_list"])):
                    crd = info[self.name]["cource_list"][i]["credit"]
                    ans += pointsToGPA(info[self.name]["cource_list"][i]["grade"]) * crd
                    credit += crd
            except:
                print("No subscription to cources")
            ans = ans / credit
            return str(ans) + ' - ' + gpaToLetter(ans)

    def seeTeachers(self):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            for key in info:
                if info[key]["role"] == 'teacher':
                    print(key + " " + info[key]["cource_list"][0]["name"])

    def showFreeCources(self):
        with open('db_courses.json', 'r') as f:
            info = json.load(f)
            for key in info:
                if info[key]["free"]:
                    print(key)

    def rateTeacher(self,nameOfTeacher, rate):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for key in info:
                    if info[key]["role"] == 'teacher' and key == nameOfTeacher:
                        info[key]["rate"].append(rate)
            except:
                print("Bad credentials")

        with open('db_users.json', 'w') as f:
            json.dump(info, f)

    def subToCourse(self, courseName):
        course = {"name": courseName}

        with open("db_courses.json", 'r') as f:
            info = json.load(f)
            course.update(info[courseName])

        with open("db_users.json", 'r') as f:
            info1 = json.load(f)
            info1[self.name]["cource_list"].append(course)

        with open("db_users.json", 'w') as f:
            json.dump(info1, f)

    def unsubFromCourse(self, courseName):

        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for i in range(0, len(info[self.name]["cource_list"])):
                    if info[self.name]["cource_list"][i]["name"] == courseName:
                        del info[self.name]["cource_list"][i]
            except:
                print("Bad credentials")

        with open('db_users.json', 'w') as f:
            json.dump(info, f)

class Teacher:
    def __init__(self, name, password, rate: [int]):
        self.name = name
        self.password = password
        self.rate = rate

    def getSubjectList(self):
        with open("db_users.json", 'r') as f:
            info1 = json.load(f)
            try:
                return info1[self.name]["cource_list"]
            except:
                return None
    def gradeStudent(self, name, nameOfSub, grade):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for i in range(0, len(info[name]["cource_list"])):
                    if info[name]["cource_list"][i]["name"] == nameOfSub:
                        info[name]["cource_list"][i]["grade"] = grade
            except:
                print("Bad credentials")

        with open('db_users.json', 'w') as f:
            json.dump(info, f)

    def subStudentToCourse(self, name, nameOfStud):
        course = {"name" : name}

        with open("db_courses.json", 'r') as f:
            info = json.load(f)
            course.update(info[name])

        with open("db_users.json", 'r') as f:
            info1 = json.load(f)
            info1[nameOfStud]["cource_list"].append(course)

        with open("db_users.json", 'w') as f:
            json.dump(info1, f)

    def unsubStudentToCourse(self, name, nameOfStud):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for i in range(0, len(info[nameOfStud]["cource_list"])):
                    if info[nameOfStud]["cource_list"][i]["name"] == name:
                        del info[nameOfStud]["cource_list"][i]
            except:
                print("Bad credentials")

        with open('db_users.json', 'w') as f:
            json.dump(info, f)

    def rateStudent(self, name, nameOfStud, rate):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                for i in range(0, len(info[nameOfStud]["cource_list"])):
                    if info[nameOfStud]["cource_list"][i]["name"] == name:
                        info[nameOfStud]["cource_list"][i]["attendance"] = rate
            except:
                print("Bad credentials")
        with open('db_users.json', 'w') as f:
            json.dump(info, f)

class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def addStudent(self, name, password):
        sample_json = {name : {"role" : "student", "password" : password, "cource_list" : []}}
        with open('db_users.json', 'r') as f:
            info = json.load(f)
        info.update(sample_json)
        with open('db_users.json', 'w') as f:
            json.dump(info, f)
    def updateItem(self, name, password):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                info[name]["password"] = password
            except:
                print("Bad credentials")
        with open('db_users.json', 'w') as f:
            json.dump(info, f)

    def deleteItem(self, name):
        with open('db_users.json', 'r') as f:
            info = json.load(f)
            try:
                del info[name]
            except:
                print("Bad credentials")
        with open('db_users.json', 'w') as f:
            json.dump(info, f)

    def addTeacher(self, name, password):
        sample_json = {name : {"role" : "teacher", "password" : password, "rate" : [], "cource_list" : []}}
        with open('db_users.json', 'r') as f:
            info = json.load(f)
        info.update(sample_json)
        with open('db_users.json', 'w') as f:
            json.dump(info, f)

    def addCourse(self, name, free):
        sample_json = {name : {"free" : free, "attendance" : 0, "credit" : 0, grade : 0}}
        if free:
            limit = int(input("Enter limit of the participants"))
            sample_json[name].update({"limit_of_participants" : limit})
        credit = input("Enter the name of credits")
        sample_json["credit"] = credit
        with open('db_courses.json', 'r') as f:
            info = json.load(f)
        info.update(sample_json)
        with open('db_courses.json', 'w') as f:
            json.dump(info, f)

    def updateCourse(self, name, free):
        with open('db_courses.json', 'r') as f:
            info = json.load(f)
            try:
                info[name]["free"] = free
            except:
                print("Bad credentials of course")
        with open('db_courses.json', 'w') as f:
            json.dump(info, f)

    def addStudentToCourse(self, name, nameOfStud):
        course = {"name" : name}
        with open("db_courses.json", 'r') as f:
            info = json.load(f)
            course.update(info[name])
        with open("db_users.json", 'r') as f:
            info1 = json.load(f)
            info1[nameOfStud]["cource_list"].append(course)
        with open("db_users.json", 'w') as f:
            json.dump(info1, f)

    def addTeacherToCourse(self, courseName, teacherName):

        course = {"name" : courseName}

        with open("db_courses.json", 'r') as f:
            info = json.load(f)
            course.update(info[courseName])

        with open("db_users.json", 'r') as f:
            info1 = json.load(f)
            info1[teacherName]["cource_list"].append(course)

        with open("db_users.json", 'w') as f:
            json.dump(info1, f)

while True:

    username = input("Enter username:")
    password = input("Enter password:")

    if getLogin(username, password):

        role = getItemRole(username)

        while True:

            if role == "admin":
                admin = Admin(username, password)
                print("0 - Log out")
                print("1 - add course")
                print("2 - update course")
                print("3 - delete course")
                print("4 - add student")
                print("5 - update student")
                print("6 - delete student")
                print("7 - add course to student")
                print("8 - add teacher")
                print("9 - update teacher")
                print("10 - delete teacher:")
                print("11 - add teacher to course:")

                type = int(input())

                if type == 1:
                    courseName = input("Enter name of the course:")
                    courseFree = bool(input("Is this course free or not? true/false:"))
                    admin.addCourse(courseName, courseFree)
                elif type == 2:
                    courseName = input("Enter name of the course:")
                    courseFree = bool(input("Is this course free or not? true/false:") == "true")
                    admin.updateCourse(courseName, courseFree)
                elif type == 3:
                    courseName = input("Enter name of the course:")
                    admin.deleteItem(courseName)
                elif type == 4:
                    studentName = input("Enter name of the student:")
                    studentPassword = input("Enter password of the student:")
                    admin.addStudent(studentName, studentPassword)
                elif type == 5:
                    studentName = input("Enter name of the student:")
                    studentPassword = input("Enter password of the student:")
                    admin.updateItem(studentName, studentPassword)
                elif type == 6:
                    studentName = input("Enter name of the student:")
                    admin.deleteItem(studentName)
                elif type == 7:
                    courseName = input("Enter name of the course:")
                    studentName = input("Enter name of the student:")
                    admin.addStudentToCourse(courseName, studentName)
                elif type == 8:
                    teacherName = input("Enter name of the teacher:")
                    teacherPassword = input("Enter password of the teacher:")
                    admin.addTeacher(teacherName, teacherPassword)
                elif type == 9:
                    teacherName = input("Enter name of the teacher:")
                    teacherPassword = input("Enter password of the teacher:")
                    admin.updateItem(teacherName, teacherPassword)
                elif type == 10:
                    teacherName = input("Enter name of the teacher:")
                    admin.deleteItem(teacherName)
                elif type == 11:
                    courseName = input("Enter name of the course:")
                    teacherName = input("Enter name of the teacher:")
                    admin.addTeacherToCourse(courseName, teacherName)
                else:
                    break

            elif role == "teacher":
                print("0 - Log Out")
                print("1 - rate student [0-100]")
                print("2 - set grade to the student")
                print("3 - see your subjects")
                print("4 - add/remove course from student")

                type = int(input())

                teacher = Teacher(username, password, [])

                if type == 1:
                    username = input("Enter name of the course:")
                    studentName = input("Enter name of the student:")
                    rate = int(input("Enter rate of the student:"))
                    teacher.rateStudent(username, studentName, rate)
                elif type == 2:
                    username = input("Enter name of the student:")
                    grade = int(input("Enter grade:"))
                    course = input("Enter course:")
                    teacher.gradeStudent(username, course, grade)
                elif type == 3:
                    print("Your subjects are:")
                    print(teacher.getSubjectList())
                elif type == 4:
                    type2 = input("sub/unsub student from course?")
                    courseName = input("Enter name of the course:")
                    studentName = input("Enter name of the student:")
                    if type2 == 'sub':
                        teacher.subStudentToCourse(courseName, studentName)
                    elif type2 == 'unsub':
                        teacher.unsubStudentToCourse(courseName, studentName)
                else:
                    break

            elif role == "student":
                student = Student(username, password)
                print("0 - Log out")
                print("1 - see all grades")
                print("2 - seeFreeCourses")
                print("3 - sub/unsub to course")
                print("4 - see teachers")
                print("5 - rate teacher [0-100]")
                print("6 - (Additional) show average gpa")
                type = int(input())
                if type == 1:
                    print(student.showGrades())
                elif type == 2:
                    student.showFreeCources()
                elif type == 3:
                    type2 = input("sub/unsub from course")
                    course = input("Enter name of the course:")
                    if type2 == 'sub':
                        student.subToCourse(courseName)
                    elif type2 == 'unsub':
                        student.unsubFromCourse(courseName)
                elif type == 4:
                    student.seeTeachers()
                elif type == 5:
                    username = input("Enter name of teacher:")
                    rate = int(input("Enter rate:"))
                    student.rateTeacher(username, rate)
                elif type == 6:
                    print(student.showAvgGPA())
                else:
                    break

    else:
        print("Error! Bad credentials")


