# python3
import sys
import threading
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
WorkerStatus = namedtuple("WorkerStatus", ["worker", "finish_time"])


def parent_of_node(i):
    """
    Index of parent node of some node with index i
    """
    return (i - 1) // 2


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


def compare_workers(w1, w2):
    """
    Compare two WorkerStatus tuples. If they have different finish time, returned is first worker has smaller finish
    time, else returned is first worker has smaller index.
    :param w1: first worker
    :param w2: second worker
    :return: True or False
    """
    if w1[1] != w2[1]:
        return w1[1] < w2[1]
    else:
        return w1[0] < w2[0]


def sift_up(arr, i):
    """
    Method, that moving element closer to the root.
    :param arr: global list of integers
    :param i: index of element
    :return: modified list arr
    """
    while i > 0 and compare_workers(arr[i], arr[parent_of_node(i)]):
        arr[parent_of_node(i)], arr[i] = arr[i], arr[parent_of_node(i)]
        i = parent_of_node(i)
    return arr


def sift_down(arr, n, i):
    """
    Method, that finds right position for element with index i in array arr.
    Assume that arr[i] is parent for two elements: right_children and left_children. We find least element between this
    three and swaps if needed least element with parent. Then we repeat this operation, where parent element is that
    with which ex-parent was swapped.
    :param arr: global list of integers
    :param n: size of list
    :param i: index, parent element
    :return: modified list arr
    """
    min_index = i

    left = left_child(i)

    if left < n and compare_workers(arr[left], arr[min_index]):
        min_index = left

    right = right_child(i)

    if right < n and compare_workers(arr[right], arr[min_index]):
        min_index = right

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        arr = sift_down(arr, n, min_index)

    return arr


def change_priority(arr, i, p):
    """
    Method, that changes priority of node with index i to value p. After that, method normalizes heap by sifting
    element up or down depending on the fact is new value more than old.
    Returns modified list.
    :param arr: global list of integers
    :param i: index of element
    :param p: new value of priority
    :return: modified list AssignedJob objects
    """
    old_p = arr[i][1]
    arr[i] = WorkerStatus(arr[i][0], p)

    if p < old_p:
        arr = sift_up(arr, i)
    else:
        arr = sift_down(arr, len(arr), i)

    return arr


def assign_jobs(n_workers, jobs):
    """
    Simulates process of jobs execution in parallel. For given amount of workers determine by which worker and when
    each job will be started.
    For solving these problem used n-ary priority min-heap. On each step at first position is stored worker that is free
    or will be free sooner  than another. This is possible if we add to the first element time of process of job and
    shift this element on corresponding place.
    :param n_workers: integer from 1 to 10**5 - number of workers
    :param jobs: list of integers, each from 1 to 10**5, list of jobs duration
    :return: returns list of
    """

    result = list()
    worker_heap = [WorkerStatus(i, 0) for i in range(n_workers)]
    for job in jobs:
        result.append(AssignedJob(worker_heap[0][0], worker_heap[0][1]))
        worker_heap = change_priority(worker_heap, 0, worker_heap[0][1] + job)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
