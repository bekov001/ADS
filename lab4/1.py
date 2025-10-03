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

n, q = map(int, input().split())
root = None
values = list(map(int, input().split()))
for v in values:
    root = push(root, v)


def trace(letter, node):
    if letter == "R":
        return node.right if node.right else None
    else:
        return node.left if node.left else None

for _ in range(q):
    path = input()
    node = root
    i = 0
    for letter in path:
        node = trace(letter, node)
        i += 1
        if node is None:
            break
    else:
        if i == len(path):
            print("YES")
            continue
    print("NO")