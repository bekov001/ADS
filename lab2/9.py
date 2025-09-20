class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

t = int(input())



for _ in range(t):
    n = int(input())
    data = list(input().split())
    res = []
    used = set()
    head = Node(data[0])
    for el in data[1:]:
        if el not in used:
            per = Node(el, head)
            head.next = per
            head = per
            res.append(head.val)
        elif el in used:
            last = head
            while last.prev is not None:
                prev = last.prev
                if prev.val not in used:
                    res.append(prev.val)
                    break
            else:
                res.append(-1)
        used.add(el)
    print(*res)