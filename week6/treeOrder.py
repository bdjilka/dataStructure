# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    """
    Implementation of basic binary tree traversal:
        - pre order
        - post order
        - in order
    All this traversals is depth based.
    """
    def __init__(self):
        self.ino = list()
        self.preo = list()
        self.posto = list()

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, index):
        if index >= self.n:
            return
        if self.left[index] > -1:
            self.inOrder(self.left[index])
        self.ino.append(self.key[index])
        if self.right[index] > -1:
            self.inOrder(self.right[index])

    def preOrder(self, index):
        if index >= self.n:
            return
        self.preo.append(self.key[index])
        if self.left[index] > -1:
            self.preOrder(self.left[index])
        if self.right[index] > -1:
            self.preOrder(self.right[index])

    def postOrder(self, index):
        if index >= self.n:
            return
        if self.left[index] > -1:
            self.postOrder(self.left[index])
        if self.right[index] > -1:
            self.postOrder(self.right[index])
        self.posto.append(self.key[index])


def main():
    """
    Input:
        5               // number of nodes n, 1 <= n <= 10**5
        4 1 2           // 0 node, key k = 4, index of left child - 1, right child is 2
        2 3 4           // 0 <= k <= 10**9
        5 -1 -1         // if index of child -1 => node is leaf
        1 -1 -1
        3 -1 -1
    Output:
    """

    # import datetime
    # t1 = datetime.datetime.now()

    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    tree.preOrder(0)
    tree.postOrder(0)
    print(" ".join(str(x) for x in tree.ino))
    print(" ".join(str(x) for x in tree.preo))
    print(" ".join(str(x) for x in tree.posto))

    # print(len(tree.right))
    # print(len(tree.left))
    # print(len(tree.key))
    # print(tree.n)
    # print(datetime.datetime.now() - t1)


threading.Thread(target=main).start()
