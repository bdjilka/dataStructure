# python3
import datetime
import sys
import threading
from collections import namedtuple

Node = namedtuple("Node", ["index", "parent", "children"])


def compute_height(n, parents):
    """
    Compute height of balanced binary search tree.

    If the i-th one of input (0 ≤ i ≤ n − 1) is −1, node i is the root, otherwise it’s 0-based index of the parent of
    i-th node. It is guaranteed that there is exactly one root. It is guaranteed that the input represents a tree.

    Firstly we create tree structure, represented by array of nodes. Node has its index, parent and children elements.
    If parent is -1 than node is root, children are array of indexes, if there is no children, than node is leave.
    Then we compute height using depth approach.

    :param n: number of nodes (from 1 to 10**5)
    :param parents: integer numbers from −1 to [n − 1] — parents of nodes
    :return: height of tree
    """
    t1 = datetime.datetime.now()

    if n == 0:
        return 0

    nodes = [0 for i in range(n)]
    root = None
    for i in range(n):
        nodes[i] = Node(i, parents[i], list())

    for i in range(n):
        parent = nodes[i].parent
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i].index)

    max_height = preOrder(nodes, root.index, 1)

    t2 = datetime.datetime.now()
    # print(t2 - t1)

    return max_height


def preOrder(nodes, vertex, height):
    """
    Calculates height of tree using depth-based approach. We start from the root element, than for each node we
    calculate heights of left and right node and saves local maximum
    :param nodes: array of nodes, where nodes i is on i-th position
    :param vertex: index of current vertex
    :param height: local height of subtree
    :return: maximum local height
    """
    node = nodes[vertex]
    max_h = height
    local_h = 0
    if node:
        for children in node.children:
            local_h = preOrder(nodes, children, height + 1)
            max_h = max(local_h, max_h)
        return max_h
    else:
        return 1


def main():
    """
    Input sample:
    5
    4 -1 4 1 1
    """
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
