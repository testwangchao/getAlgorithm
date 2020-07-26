from link_list.linked_list import LinkList


def del_repeat_node(node):
    """
    移除未排序链表中的重复节点。保留最开始出现的节点。
    """
    if not node:
        return node
    node_set = set({node.val})
    cur = node
    """
    此处如果使用cur，如果最后一个节点的val已经出现过，比如[1,2,3,3,2,1]，
    最后一个节点的值1已经出现过，此时当前的节点没有办法删除，故使用cur.next，
    所以初始化集合的时候，需要把第一个节点就放入集合内
    """
    while cur.next:
        if cur.next.val not in node_set:
            node_set.add(cur.next.val)
            cur = cur.next
        else:
            cur.next = cur.next.next
    return node
