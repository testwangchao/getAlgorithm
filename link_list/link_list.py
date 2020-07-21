class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class LinkList:
    def __init__(self, node=None):
        self._head = node

    # 头部插入
    def add(self, val):
        node = ListNode(val)
        if not self._head:
            self._head = node
            return
        node.next = self._head
        self._head = node

    # 尾部插入
    def append(self, val):
        node = ListNode(val)
        if not self._head:
            self._head = node
            return
        cur = self._head
        while cur.next:
            cur = cur.next
        cur.next = node

    # 指定位置插入
    def insert(self, index, val):
        node = ListNode(val)
        if index == 0:
            self.add(val)
        else:
            cur = self._head
            for _ in range(1, index):
                cur = cur.next
            node.next = cur.next
            cur.next = node
            # prev_node = cur.next
            # cur.next = node
            # node.next = prev_node
    

if __name__ == '__main__':
    lt = LinkList()
    # lt.add(4)
    # lt.add(5)
    # lt.add(6)
    lt.append(7)
    # lt.append(8)
    lt.insert(1, 9)
    lt.add(6)
    lt.insert(2,77)
    # lt.insert(3,2)
    # lt.insert(4,5)
    pass
