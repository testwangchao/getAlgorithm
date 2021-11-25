from link_list.linked_list import LinkList


def deleteDuplicates(head):
    """
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    """
    if head is None or head.next is None:
        return head
    # 定义一个哑结点
    dummy, dummy.next = LinkList(0), head
    while head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return dummy.next


def deleteDuplicates2(head):
    if head is None or head.next is None:
        return head
    cur = head
    val_set = set({head.val})
    while cur.next:
        if cur.val = cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

