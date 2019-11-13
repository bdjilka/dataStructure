#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def checkNode(tree, index, lower, upper, is_right):
    """
    Recursive function that checks if given node satisfies condition of binary search tree. Then called checks for
    left and right child nodes of input one.
    :param tree: list of nodes
    :param index: index of current node
    :param lower: lower bound of allowable interval of keys for node
    :param upper: upper bound of allowable interval of keys for node
    :param is_right: indicates whether it is right subtree of anything
    :return: True/False
    """
    if not is_right:
        if not lower < tree[index][0] < upper:
            return False
    else:
        if not lower <= tree[index][0] < upper:
            return False

    if tree[index][1] > -1:
        if not checkNode(tree, tree[index][1], lower, tree[index][0], False or is_right):
            return False

    if tree[index][2] > -1:
        if not checkNode(tree, tree[index][2], tree[index][0], upper, True):
            return False

    return True


def IsBinarySearchTree(tree):
    """
    Implementation of check whether given tree is a binary search tree.
    :param tree: list if nodes with information about key, indexes of left and right nodes
    :return: True/False

    The point is that this case allows duplicates: for any node of the tree, if its key is x, then for any node in its
    left subtree its key must be strictly less than x, and for any node in its right subtree its key must be greater
    than or equal to x.
    """
    key = tree[0][0]
    bound = pow(2, 31)
    if tree[0][1] > -1:
        if not checkNode(tree, tree[0][1], -bound - 1, key, False):
            return False
    if tree[0][2] > -1:
        if not checkNode(tree, tree[0][2], key, bound, True):
            return False
    return True


def main():
    """
    Input:
        3               // number of nodes n, 0 <= n <= 10**5
        2 1 2           // 0 node, key - left child - right child
        1 -1 -1         // 1-st node
        3 -1 -1         // -2**31 <= key <= 2**31 - 1, if left child is -1 => no child
    Output:
    """
    nodes = int(sys.stdin.readline().strip())
    tree = list()
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if len(tree) == 0:
        print("CORRECT")
    elif len(tree) == 1:
        if -pow(2, 31) <= tree[0][0] < pow(2, 31):
            print("CORRECT")
    else:
        if IsBinarySearchTree(tree):
            print("CORRECT")
        else:
            print("INCORRECT")


threading.Thread(target=main).start()
