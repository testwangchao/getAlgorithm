from link_list.linked_list import LinkList


def kthToLast(head, index):
    """
    返回倒数第K个节点,快慢指针
    """
    cur1 = head
    cur2 = head
    for i in range(index):
        cur2 = cur2.next

    while cur2:
        cur2 = cur2.next
        cur1 = cur1.next
    return cur1.val
