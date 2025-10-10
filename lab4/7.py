import sys
sys.setrecursionlimit(300000)


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
def dfs(u):

    global ans
    if u is None:
        return 0
    hl = dfs(u.left)
    hr = dfs(u.right)
    if hl + hr + 1 > ans:
        ans = hl + hr + 1
    return max(hl, hr) + 1

dfs(root)
print(ans)