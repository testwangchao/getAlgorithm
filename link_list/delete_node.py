from link_list.linked_list import LinkList


def delete_node(head, val):
    """
    删除链表中的某一个节点，非头结点和尾节点
    """
    cur = head
    while cur:
        if cur.val == val:
            cur.val = cur.next.val
            cur.next = cur.next.next
        else:
            cur = cur.next


if __name__ == '__main__':
    lt = LinkList()
    lt.add(1)
    lt.append(1)
    lt.append(4)
    lt.insert(3, 88)
    lt.append(5)
    lt.append(6)
    lt.append(7)
    head = lt._head
    delete_node(head, 88)
    pass
