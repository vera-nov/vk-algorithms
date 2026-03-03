from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head: Optional[Node]) -> Optional[Node]:
    curr = head
    prev = None
    while curr and curr.next:
        temp = curr
        curr = curr.next
        temp.next = prev
        prev = temp
    if curr:
        curr.next = prev
    return curr

