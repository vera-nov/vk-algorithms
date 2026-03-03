from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeLinkedListElement(head: Optional[Node], val: int) -> Optional[Node]:
    dummy_head = Node(-1, head)
    prev = dummy_head
    while head:
        if head.val == val:
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return dummy_head.next