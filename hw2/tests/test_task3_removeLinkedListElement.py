from solutions.task3_removeLinkedListElement import Node, removeLinkedListElement
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
    res: List[int] = []
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
    ids: List[int] = []
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
    "values, val, expected",
    [
        # empty list
        ([], 1, []),

        # single element
        ([1], 1, []),
        ([1], 2, [1]),

        # all elements removed
        ([7, 7, 7], 7, []),

        # remove head (single and multiple head duplicates)
        ([5, 1, 2, 3], 5, [1, 2, 3]),
        ([5, 5, 1, 2], 5, [1, 2]),

        # remove middle element(s)
        ([1, 2, 3, 4], 3, [1, 2, 4]),
        ([1, 2, 2, 2, 3], 2, [1, 3]),

        # remove tail element(s)
        ([1, 2, 3], 3, [1, 2]),
        ([1, 2, 3, 3], 3, [1, 2]),

        # no removals
        ([1, 2, 3, 4], 99, [1, 2, 3, 4]),

        # alternating removals
        ([1, 2, 1, 2, 1, 2], 1, [2, 2, 2]),
    ],
)
def test_remove_values(values, val, expected):
    head = build_list(values)
    new_head = removeLinkedListElement(head, val)
    assert to_list(new_head) == expected


def test_no_cycle_created():
    values = [1, 2, 3, 2, 4, 2, 5]
    head = build_list(values)
    new_head = removeLinkedListElement(head, 2)
    assert to_list(new_head) == [1, 3, 4, 5]


def test_structure_unchanged_when_val_not_present():
    values = [10, 20, 30]
    head = build_list(values)

    ids_before = collect_node_ids(head)
    vals_before = to_list(head)

    new_head = removeLinkedListElement(head, 999)

    assert to_list(new_head) == vals_before
    assert collect_node_ids(new_head) == ids_before


def test_remove_last_node_when_head_has_no_next():
    head = build_list([67])
    new_head = removeLinkedListElement(head, 67)
    assert new_head is None