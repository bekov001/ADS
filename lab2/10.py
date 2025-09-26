import sys

class Node:
    __slots__ = ("data", "next")
    def __init__(self, data):
        self.data = data
        self.next = None

def findMaxSum(head: Node) -> int:
    cur = best = head.data
    p = head.next
    while p:
        x = p.data
        cur = x if cur + x < x else cur + x
        best = best if best >= cur else cur
        p = p.next
    return best


data = sys.stdin.read().strip().split()
if not data:
    exit(0)
it = iter(data)
N = int(next(it))
head = tail = None
for _ in range(N):
    x = int(next(it))
    node = Node(x)
    if head is None:
        head = tail = node
    else:
        tail.next = node
        tail = node
if head is None:
    print(0)
else:
    print(findMaxSum(head))


