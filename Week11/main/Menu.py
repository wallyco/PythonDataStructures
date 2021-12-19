from main import Login

def menu(student):

    userinput = str(input(""""Enter '1' to Add a course|
       '2' to Drop a course|
       '3' to View your courses|
       '4' logout|
       '5' exit|
        """))
    if userinput == "1":
        # userinput for course name to add
        student.addCourse(input("Enter a course to add: "))
        menu(student)
    elif userinput == "2":
        # userinput for course name to drop
        student.removeCourse(input("Enter a course to add: "))
        menu(student)
    elif userinput == "3":
        student.showCourses()
        menu(student)
    elif userinput == "4":
        print("Exiting to login")
        menu(Login())
    elif userinput == "5":
        print("Good bye")
        return
    else:
        print("That option is invalid")
        menu(student)