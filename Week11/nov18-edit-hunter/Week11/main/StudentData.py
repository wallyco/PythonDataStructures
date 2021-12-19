class StudentData:

    def __init__(self, id=None, course=None):
        self.data = {
            "StudentId" : id,
            "StudentCourse" : course
        }
        self.size = 0

    def add(self, course):
        if course not in self.data.get("StudentCourse"):
            self.data.get("StudentCourse").add(course)
            print(f"Course '{course}' added.")
            self.size += 1
        else:
            print(f"Course '{course}' already registered.")
        pass

    def remove(self, course):
        if course in self.data.get("StudentCourse"):
            self.data.get("StudentCourse").remove(course)
            print(f"Course '{course}' dropped.")
            self.size -= 1
        else:
            print(f"Course '{course}' not found in registered courses.")

        pass

    def coursesToString(self):
        if self.size == 0:
            return print("You have no courses to display")
        return print(self.data["StudentCourse"])
