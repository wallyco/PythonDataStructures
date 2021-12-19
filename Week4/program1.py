list = [2, 5, 7, 9, 14, 27]


def linearSearchSorted(target, list):
    visited = []
    found = -1
    i = 0
    while i in range(len(list)):
        visited.append(list[i])
        if list[i] > target:
            break
        if list[i] == target:
            found = i
            break
        i += 1

    toString(list, target, visited, found)


def toString(list, target, visited, found):
    print("List: ", list)
    print("Search target", target)
    print("Elements visited: ", visited)
    if found >= 0:
        print("Target found at position: ", found)
    else:
        print("Target not found")
    print("")


def main():
    linearSearchSorted(2, list)
    linearSearchSorted(6, list)
    linearSearchSorted(14, list)
    linearSearchSorted(27, list)
    linearSearchSorted(28, list)


if __name__ == "__main__":
    main()
