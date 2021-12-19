from main.StudentData import StudentData


class Student:

    def __init__(self, name=None, id=None, course=None):
        self.name = name
        self.id = id
        self.data = StudentData(id, course)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setID(self, id):
        self.id = id

    def addCourse(self, course):
        self.data.add(course)

    def removeCourse(self, course):
        self.data.remove(course)

    def showCourses(self):
        self.data.coursesToString()