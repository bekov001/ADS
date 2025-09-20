class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n, k = map(int, input().split())
data = input().split()

head = Node(data[0])
curr = head
for word in data[1:]:
    node = Node(word)
    curr.next = node
    curr = node

length = n
k %= length
if k == 0:
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    exit()

new_tail = head
for _ in range(k - 1):
    new_tail = new_tail.next

new_head = new_tail.next
new_tail.next = None

curr = new_head
while curr.next:
    curr = curr.next
curr.next = head

curr = new_head
while curr:
    print(curr.data, end=" ")
    curr = curr.next