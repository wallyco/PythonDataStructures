def main():
    hourlyWage = float(input("Enter hourly wage: $"))
    hour = float(input("Enter the regular hours "))
    overtime = float(input("Enter the overtime hours "))

    overtimeWage = hourlyWage * 1.5
    sum = hourlyWage * hour + overtimeWage * overtime;

    print("The total weekly pay is: $%.2f" % sum)


if __name__ == "__main__":
    main()
