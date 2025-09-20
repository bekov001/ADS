import sys

class Node:
    def __init__(self, val=0, next=None):
        self.val: str = val
        self.next: "Node" | None = next

class Solution:
    def __init__(self):
        self.head: Node | None = None

    def add_front(self, name: str):
        node = Node(name, self.head)
        self.head = node
        print("ok")

    def add_back(self, name: str):
        node = Node(name)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        print("ok")

    def erase_front(self):
        if self.head is None:
            print("error")
            return
        print(self.head.val)
        self.head = self.head.next

    def erase_back(self):
        if self.head is None:
            print("error")
            return
        if self.head.next is None:  # только один элемент
            print(self.head.val)
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        print(cur.next.val)
        cur.next = None

    def front(self):
        if self.head is None:
            print("error")
        else:
            print(self.head.val)

    def back(self):
        if self.head is None:
            print("error")
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            print(cur.val)

    def clear(self):
        self.head = None
        print("ok")

    def main(self):
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            if line == "exit":
                print("goodbye")
                break

            parts = line.split(maxsplit=1)
            cmd = parts[0]

            if cmd == "add_front":
                self.add_front(parts[1])
            elif cmd == "add_back":
                self.add_back(parts[1])
            elif cmd == "erase_front":
                self.erase_front()
            elif cmd == "erase_back":
                self.erase_back()
            elif cmd == "front":
                self.front()
            elif cmd == "back":
                self.back()
            elif cmd == "clear":
                self.clear()
            else:
                pass

s = Solution()
s.main()
