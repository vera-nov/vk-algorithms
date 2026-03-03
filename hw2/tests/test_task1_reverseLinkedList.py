from solutions.task1_reverseLinkedList import Node, reverseLinkedList
from typing import List, Optional
import pytest

def build_list(values: List[int]) -> Optional[Node]:
    """
    Create a singly linked list out of an array
    """
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head: Optional[Node]) -> List[int]:
    """
    Create an array out of a singly linked list
    """
    res = []
    seen = set()
    cur = head
    while cur is not None:
        obj_id = id(cur)
        if obj_id in seen:
            raise AssertionError("Cycle detected in linked list")
        seen.add(obj_id)
        res.append(cur.val)
        cur = cur.next
    return res


def collect_node_ids(head: Optional[Node]) -> List[int]:
    """
    Collect id of all nodes (in-place check)
    """
    ids = []
    seen = set()
    cur = head
    while cur is not None:
        obj_id = id(cur)
        if obj_id in seen:
            raise AssertionError("Cycle detected in linked list")
        seen.add(obj_id)
        ids.append(obj_id)
        cur = cur.next
    return ids


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([3, 6, 8, 4, 7, 9, 11], [11, 9, 7, 4, 8, 6, 3]),
        ([-1, 0, -1, 2], [2, -1, 0, -1]),
    ],
)
def test_reverse_values(values, expected):
    head = build_list(values)
    new_head = reverseLinkedList(head)
    assert to_list(new_head) == expected


def test_reverse_none_head():
    assert reverseLinkedList(None) is None


def test_in_place_same_nodes_reused():
    values = [1, 2, 3, 4, 5]
    head = build_list(values)

    before_ids = set(collect_node_ids(head))
    new_head = reverseLinkedList(head)
    after_ids = set(collect_node_ids(new_head))

    assert before_ids == after_ids


def test_tail_next_is_none_after_reverse():
    values = [10, 20, 30, 40]
    head = build_list(values)
    new_head = reverseLinkedList(head)

    cur = new_head
    while cur.next is not None:
        cur = cur.next
    assert cur.next is None


def test_no_cycle_created():
    values = list(range(1, 100))
    head = build_list(values)
    new_head = reverseLinkedList(head)

    out = to_list(new_head)
    assert out == list(reversed(values))


def test_double_reverse_returns_original_order():
    values = [1, 2, 3, 4, 5, 6]
    head = build_list(values)

    r1 = reverseLinkedList(head)
    r2 = reverseLinkedList(r1)
    assert to_list(r2) == values