courseList = []


def optionA():
    newcourse = str(input("  Enter a course to add: "))

    if newcourse in courseList:
        print("  You are already registered to that class")
    else:
        courseList.append(newcourse)
        print("  %s added" % newcourse)
        courseList.sort()
        print("Current Course List:\n %s \n" % courseList)


def optionD():
    dropcourse = str(input("  Enter a course to drop: "))

    if dropcourse not in courseList:
        print("  You are not registered to that class")
    else:
        courseList.remove(dropcourse)
        print("  %s dropped" % dropcourse)
        print("Current Course List:\n %s \n" % courseList)


def menu():
    userinput = str(input(""""Enter 'A' to add a class: 'D' to drop a class: or 'E' to exit"  """)).lower()
    if userinput == "a":
        optionA()
        menu()
    elif userinput == "d":
        optionD()
        menu()
    elif userinput == "e":
        print("Goodbye")
        return
    else:
        print("That option is invalid")
        menu()


def main():
    menu()


if __name__ == "__main__":
    main()
