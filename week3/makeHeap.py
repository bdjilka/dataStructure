# python3
import datetime


def build_heap_naive(data):
    """
    Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def left_child(i):
    """
    Index of left child of node with index i
    """
    return 2 * i + 1


def right_child(i):
    """
    Index of right child of node with index i
    """
    return 2 * i + 2


def sift_down(swaps, arr, n, i):
    """
    Method, that finds right position for element with index i in array arr.
    Assume that arr[i] is parent for two elements: right_children and left_children. We find least element between this
    three and swaps if needed least element with parent. Then we repeat this operation, where parent element is that
    with which ex-parent was swapped.
    :param swaps: global array of swaps
    :param arr: global list of integers
    :param n: size of list
    :param i: index, parent element
    :return: modified swaps
    """
    min_index = i
    l = left_child(i)
    if l < n and arr[l] < arr[min_index]:
        min_index = l

    r = right_child(i)
    if r < n and arr[r] < arr[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps = sift_down(swaps, arr, n, min_index)

    return swaps


def build_heap(arr, n):
    """
    Build a heap from array of integers using no more than 4n swaps.
    Returns a sequence of swaps performed by the algorithm.
    :param arr: list of integers from 0 to 10**9
    :param n: length of list from 1 to 10**5
    :return: array od swaps
    """
    swaps = list()
    for i in range((n - 1) // 2, -1, -1):
        swaps = sift_down(swaps, arr, n, i)
    return swaps


def main():
    """
    Input sample:
    5               # n = 5 elements
    5 4 3 2 1       # array of numbers
    Output sample:
    3               # number of swaps
    1 4             # swap of elements with indexes 1 and 4
    0 1             # second swap array[0] and array[1]
    1 3             # last swap array[1] and array[3]
    """

    # t1 = datetime.datetime.now()

    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data, n)

    # t2 = datetime.datetime.now() - t1
    # print(t2)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
