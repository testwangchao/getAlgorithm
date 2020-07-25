from link_list.linked_list import LinkList


def reverse_link_list(node):
    """
    反转链表
    """
    cur = node
    new_node = None
    while cur:
        prev = cur
        cur = cur.next
        prev.next = new_node
        new_node = prev
    return new_node


if __name__ == '__main__':
    lt = LinkList()
    lt.add(1)
    lt.append(1)
    lt.append(4)
    lt.insert(3, 88)
    lt.append(5)
    lt.append(6)
    lt.append(7)
    node = lt._head
    reverse_link_list(node)
