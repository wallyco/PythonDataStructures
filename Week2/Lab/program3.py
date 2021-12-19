lastName = ""
hourlyRate = 0.0
hoursWorked = 0


def openFile():
    file = open("payroll_data.txt", 'r')
    print("NAME:       RATE:       HOURS:       TOTAL PAY:")
    for line in file:
        line_items = line.split()
        lastName = line_items[0]
        hourlyRate = float(line_items[1])
        hourWorked = float(line_items[2])
        totalpay = hourlyRate * hourWorked
        print("%s        %.2f        %.1f        %.2f" % (lastName, hourlyRate, hourWorked, totalpay))


def main():
    openFile()


if __name__ == "__main__":
    main()
