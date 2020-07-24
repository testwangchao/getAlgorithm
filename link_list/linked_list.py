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

    # 删除节点
    def remove(self, val):
        if self._head.val == val:
            self._head = self._head.next
            return
        cur = self._head
        # 快慢指针，如果快指针找到目标值，就将慢指针的下一个节点指向目标节点的下一个节点
        pre1 = cur
        pre2 = cur.next
        # while cur.next:
        #     if cur.next.val == val:
        #         prev = cur.next.next
        #         cur.next = prev
        #         return
        #     else:
        #         cur = cur.next
        # if cur.next.val == val:
        #     cur.next = None
        # return self._head
        while pre2:
            if pre2.val == val:
                pre1.next = pre2.next
                return
            else:
                pre2 = pre2.next
                pre1 = pre1.next
        return self._head

    # 查找节点元素的位置
    def serch_value(self, val):
        cur = self._head
        index = 0
        while cur:
            if cur.val == val:
                return index
            cur = cur.next
            index += 1


if __name__ == '__main__':
    lt = LinkList()
    lt.add(1)
    lt.append(1)
    lt.append(4)
    lt.insert(3, 88)
    lt.append(5)
    lt.append(6)
    lt.append(7)
    print(lt.serch_value(1))
