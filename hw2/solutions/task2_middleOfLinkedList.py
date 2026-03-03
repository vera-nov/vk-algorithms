from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[Node]) -> Optional[Node]:
    """
    If there are 2 middle nodes, return the second middle node.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
