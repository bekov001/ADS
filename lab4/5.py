from collections import deque

n = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

nodes = {}
for _ in range(n - 1):
    x, y, z = map(int, input().split())

    if x not in nodes:
        nodes[x] = Node(x)
    if y not in nodes:
        nodes[y] = Node(y)

    if z == 0:
        nodes[x].left = nodes[y]
    else:
        nodes[x].right = nodes[y]

root = nodes[1]


q = deque([root])
max_width = 0

while q:
    level_size = len(q)
    max_width = max(max_width, level_size)

    for _ in range(level_size):
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

print(max_width)