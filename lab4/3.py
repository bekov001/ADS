import sys

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
x = int(input())


def trace(x, node):
    if x > node.val:
        return trace(x, node.right)
    elif x < node.val:
        return trace(x, node.left)
    else:
        return size(node)

def size(node):
    out = []
    if node:
        stack = [node]
        while stack:
            u = stack.pop()
            out.append(str(u.val))
            if u.right: stack.append(u.right)
            if u.left:  stack.append(u.left)
    return " ".join(out)




print(trace(x, root))
