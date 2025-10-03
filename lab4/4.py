import sys
from collections import deque
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def push(node, value):
    if  node is None:
        return Node(value)
    if value < node.val:
        node.left = push(node.left, value)
    elif value > node.val:
        node.right = push(node.right, value)
    return node

n = int(input())
root = None
values = list(map(int, input().split()))
for v in values:
    root = push(root, v)
# x = int(input())


# def trace(x, node):
#     if x > node.val:
#         return trace(x, node.right)
#     elif x < node.val:
#         return trace(x, node.left)
#     else:
#         return size(node)

def summ(node):
    if root is None:
        return 0, []
    q = deque([root])
    sums = []
    while q:
        s = 0
        for _ in range(len(q)):
            u = q.popleft()
            s += u.val
            if u.left:  q.append(u.left)
            if u.right: q.append(u.right)
        sums.append(s)
    return len(sums), sums




a, b = (summ(root))
print(a)
print(*b)