class StudentData:

    def __init__(self, id=None, course=None):
        self.data = {
            "StudentId" : id,
            "StudentCourse" : course
        }

    def add(self, course):
        #if this course !contain course
            #add course
        pass

    def remove(self, course):
        #if this course contain course
            #remove course
        pass

    def coursesToString(self):
        return print(self.data["StudentCourse"])
