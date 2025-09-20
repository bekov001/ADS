class Node:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: "Node" = next


def insert(head: Node, node: Node, p: int):
    if p == 0:
        node.next = head
        return node
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    node.next = cur.next
    cur.next = node
    return head


def remove(head: Node, p: int):
    if p == 0:
        return head.next
    cur = head
    for _ in range(p - 1):
        cur = cur.next
    cur.next = cur.next.next
    return head


def printAll(head: Node):
    if head is None:
        print(-1)
        return
    vals = []
    cur = head
    while cur:
        vals.append(str(cur.val))
        cur = cur.next
    print(" ".join(vals))


def replace(head: Node, p1: int, p2: int):
    if head is None or p1 == p2:
        return head


    if p1 == 0:
        moved = head
        head = head.next
    else:
        prev = head
        for _ in range(p1 - 1):
            prev = prev.next
        moved = prev.next
        prev.next = moved.next
    moved.next = None  # отстыкуем


    if p2 == 0:
        moved.next = head
        head = moved
        return head
    cur = head
    for _ in range(p2 - 1):
        cur = cur.next
    moved.next = cur.next
    cur.next = moved
    return head


def reverse(head: Node):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def cyclic_left(head: Node, x: int):
    if head is None or head.next is None or x == 0:
        return head

    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    x %= length
    if x == 0:
        return head

    tail.next = head
    new_tail = head
    for _ in range(x - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head


def cyclic_right(head: Node, x: int):
    if head is None or head.next is None or x == 0:
        return head

    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    x %= length
    if x == 0:
        return head
    return cyclic_left(head, length - x)


head: Node = None

while True:
    vals = [int(i) for i in input().split()]
    if vals[0] == 0:
        break
    elif vals[0] == 1:
        head = insert(head, Node(vals[1]), vals[2])
    elif vals[0] == 2:
        head = remove(head, vals[1])
    elif vals[0] == 3:
        printAll(head)
    elif vals[0] == 4:
        head = replace(head, vals[1], vals[2])
    elif vals[0] == 5:
        head = reverse(head)
    elif vals[0] == 6:
        head = cyclic_left(head, vals[1])
    elif vals[0] == 7:
        head = cyclic_right(head, vals[1])