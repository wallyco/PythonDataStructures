def selectionSort(plist, reverse=False):
    il = len(plist)

    for i in range(il - 1):
        for k in range(0, il - 1):
            if (plist[k] > plist[k + 1]):
                plist[k], plist[k + 1] = plist[k + 1], plist[k]

    if reverse:
        reverselist = plist.copy()
        i = len(plist) - 1
        plist.clear()
        while i >= 0:
            plist.append(reverselist[i])
            i -= 1


def main():
    lyst1 = [2, 4, 3, 0, 1, 5]
    print("Original list:", lyst1)
    selectionSort(lyst1)
    print("Sorted in ascending order:", lyst1)

    lyst2 = [7, 2, 5, 9, 0, 1]
    print("Original list:", lyst2)
    selectionSort(lyst2, reverse=True)
    print("Sorted in descending order:", lyst2)


if __name__ == "__main__":
    main()
