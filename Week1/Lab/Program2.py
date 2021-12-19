def main():
    initialHeight = float(input("Enter the height from which the ball is dropped: "))
    bounceIndex = float(input("Enter the bounciness of the ball: "))
    numberOfBounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

    heightTemp = initialHeight
    for i in range(numberOfBounces):
        if i > 0:
            initialHeight += newBounceHeight

        newBounceHeight = heightTemp * bounceIndex
        heightTemp = newBounceHeight
        initialHeight += newBounceHeight

    print("Total distance traveled is: %.4f" % initialHeight)


if __name__ == "__main__":
    main()
