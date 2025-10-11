class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n = int(input().strip())
head = None
tail = None
for _ in range(n):
    val = int(input().strip())
    node = Node(val)
    if head is None:
        head = tail = node
    else:
        tail.next = node
        tail = node


data = int(input().strip())
position = int(input().strip())


new_node = Node(data)
if position == 0:
    new_node.next = head
    head = new_node
else:
    cur = head
    for _ in range(position - 1):
        cur = cur.next
    new_node.next = cur.next
    cur.next = new_node


cur = head
while cur:
    print(cur.data, end=" ")
    cur = cur.next