from solutions.task2_middleOfLinkedList import Node, middleNode
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
    "values, expected_middle_index",
    [
        ([1], 0),
        ([1, 2], 1),
        ([1, 2, 3], 1),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3, 4, 5], 2),
        ([10, 20, 30, 40, 50, 60], 3),
    ],
)
def test_middle_node_value(values, expected_middle_index):
    head = build_list(values)
    mid = middleNode(head)
    assert mid is not None
    assert mid.val == values[expected_middle_index]


def test_middle_node_none_for_empty_list():
    head = build_list([])
    assert middleNode(head) is None


def test_middle_node_is_existing_node_in_list():
    values = [1, 2, 3, 4, 5, 6]
    head = build_list(values)

    ids_before = set(collect_node_ids(head))
    mid = middleNode(head)
    assert mid is not None

    # returned node must be one of the existing nodes (no new allocations)
    assert id(mid) in ids_before


def test_list_structure_not_modified():
    values = [3, 6, 8, 4, 7, 9, 11]
    head = build_list(values)

    ids_before = collect_node_ids(head)
    vals_before = to_list(head)

    mid = middleNode(head)
    assert mid is not None

    # ensure original list is unchanged
    assert to_list(head) == vals_before
    assert collect_node_ids(head) == ids_before


def test_no_cycle_created():
    values = list(range(1, 200))
    head = build_list(values)
    mid = middleNode(head)
    assert mid is not None

    # to_list will raise if a cycle exists
    assert to_list(head) == values