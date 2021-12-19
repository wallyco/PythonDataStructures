from main.Menu import menu
from main.Student import Student


# josh is a sample student, and idlist and studentlist are populated with sample testable entries
josh = Student("josh", "0001", {"csc130"})
# IDList is a dict with items structured {"ID number": "Password"}
IDList = {"0001": "1234"}
# studentlist is a dict with items structured {"ID number": Student object}
studentlist = {"0001": josh}


# request user input for ID (0 = register new student)
# check ID against keys in IDList.  If present, request password; if absent, retry
# if input password matches the value at the ID key in IDList, log in; otherwise, retry
# returns a student object located at the key value in IDList
def login():
    print("Welcome to the Course Management System")
    IDinput = str(input("Enter ID to log in, or 0 to register a new ID: "))
    if IDinput == "0":
        return register()
    elif IDinput in IDList.keys():
        passwordinput = str(input("Enter Password: "))
        if IDList.get(IDinput) == passwordinput:
            print(f"Logged in as {studentlist.get(IDinput).name} ID# {IDinput}.")
            return studentlist.get(IDinput)
        else:
            print("ID/Password pair not found")
            return login()
    else:
        print("ID not found.")
        return login()

# request new student ID (0 = return to login)
# check ID against keys in IDList.  If absent, continue; if present, return to login
# request input for name and password, append to dicts and create a new student object
# returns the new student object located at the new key value in IDList
def register():
    newID = str(input("Enter new student ID or 0 to return to login: "))
    if newID =="0":
        return login()
    elif newID in IDList.keys():
        print("ID already exists.")
        return login()
    else:
        nameinput = str(input(f"Enter student name for new ID# {newID}: "))
        passwordinput = str(input(f"Enter Password for {nameinput} ID# {newID}: "))
        studentlist.update({newID: Student(nameinput, newID)})
        IDList.update({newID: passwordinput})
        print(f"Student created: Logged in as {studentlist.get(newID).name} ID# {newID}.")
        return studentlist.get(newID)

