def main():
    unitBuy = int(input("How many copies are you buying? "))
    if unitBuy <= 10:
        unitPrice = 99
    elif unitBuy <= 50:
        unitPrice = 89
    elif unitBuy <= 100:
        unitPrice = 79
    else:
        unitPrice = 69

    total = unitPrice * unitBuy

    print("Unit Price: $%s \nTotal Price: $%.2f" % (unitPrice, total))


if __name__ == "__main__":
    main()
