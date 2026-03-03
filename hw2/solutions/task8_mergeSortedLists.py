from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeSortedLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    if not list1:
        return list2
    if not list2:
        return list1
    res_head = None
    list1_curr = None
    list2_curr = None
    if list1.val < list2.val:
        list1_curr = list1.next
        list2_curr = list2
        list1.next = None
        res_head = list1
    else:
        list2_curr = list2.next
        list1_curr = list1
        list2.next = None
        res_head = list2
    res_curr = res_head
    while list1_curr and list2_curr:
        if list1_curr.val < list2_curr.val:
            res_curr.next = list1_curr
            list1_curr = list1_curr.next
            res_curr = res_curr.next
            res_curr.next = None
        else:
            res_curr.next = list2_curr
            list2_curr = list2_curr.next
            res_curr = res_curr.next
            res_curr.next = None
    if list1_curr:
        res_curr.next = list1_curr
    if list2_curr:
        res_curr.next = list2_curr
    return res_head