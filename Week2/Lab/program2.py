def median(list):
    list.sort()
    return list[int(len(list) / 2)]


def average(list):
    sum = 0.0
    for index in list:
        sum += index
    return sum / len(list)


def main():
    list = [27, 5, 18, 66, 12, 5, 9]
    print("List: ", list)
    print("Median: ", median(list))
    print("Average: ", average(list))


if __name__ == "__main__":
    main()
