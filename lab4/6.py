from collections import deque

n = int(input())
ls = list(map(int, input().split()))

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.val:
        node.left = insert(node.left, value)
    elif value > node.val:
        node.right = insert(node.right, value)
    return node

root = None
for v in ls:
    root = insert(root, v)


ans = 0
q = deque([root])
while q:
    node = q.popleft()
    if node.left and node.right:
        ans += 1
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)

print(ans)