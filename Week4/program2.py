def reverse(plist: [], start, end):
    end -= 1
    if start >= end:
        print("Start cannot be above or equal to the end value")
    if start < 0:
        print("Start cannot be below 0")
        return
    if end >= len(plist):
        print("End cannot be above the length of the list")
        return

    i = 0
    while i in range(len(plist)):
        if start != end:
            temp = plist[start]
            plist[start] = plist[end]
            plist[end] = temp
            start += 1
            end -= 1
            i += 1
        if int(start) >= int(end):
            break


def main():
    lyst = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst)

    reverse(lyst, 0, len(lyst))
    print("Reverse whole list:", lyst)

    lyst = [7, 2, 5, 9, 0, 1]
    reverse(lyst, 0, 3)
    print("Reverse first 3 elements only:", lyst)

    lyst = [7, 2, 5, 9, 0, 1]
    reverse(lyst, 1, 5)
    print("Reverse middle 4 elements only:", lyst)

    print("Try to reverse list with starting index = -1 ")
    reverse(lyst, -1, 2)

    print("Try to reverse list with ending index = 7 ")
    reverse(lyst, 0, 7)

    print("Try to reverse list with starting index >= ending index ")
    reverse(lyst, 4, 4)


if __name__ == "__main__":
    main()
