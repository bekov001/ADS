class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_every_second(head):
    cur = head
    while cur and cur.next:
        cur.next = cur.next.next
        cur = cur.next
    return head

def build_linked_list(values):
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next

n = int(input().strip())
arr = list(map(int, input().split()))

head = build_linked_list(arr)
head = delete_every_second(head)
print_linked_list(head)