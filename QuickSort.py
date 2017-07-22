def main():
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print "before sorting: ", arr
    quickSort(arr)
    print "after Sorting: ", arr


def quickSort(arr):
    qSortHelper(arr, 0, len(arr) - 1)


def qSortHelper(alist, start, end):
    if start < end:
        split_point = partition(alist, start, end)

        qSortHelper(alist, start, split_point - 1)
        qSortHelper(alist, split_point + 1, end)


def partition(alist, start, end):
    pivot = alist[start]

    leftmark = start + 1
    rightmark = end

    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark += 1

        while alist[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[start], alist[rightmark] = alist[rightmark], alist[start]
    return rightmark


if __name__ == '__main__':
    main()
