from solutions.task8_mergeSortedLists import mergeSortedLists, Node
import pytest
from typing import List, Optional


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
    "a, b, expected",
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [2], [2]),
        ([1], [1], [1, 1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([3, 6, 8], [4, 7, 9, 11], [3, 4, 6, 7, 8, 9, 11]),
        ([-10, -5, 0], [-7, -6, 3, 4], [-10, -7, -6, -5, 0, 3, 4]),
        ([1, 1, 2], [1, 3], [1, 1, 1, 2, 3]),
        ([5, 6, 7], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7]),
    ],
)
def test_merge_sorted_lists_values(a, b, expected):
    l1 = build_list(a)
    l2 = build_list(b)
    merged = mergeSortedLists(l1, l2)
    assert to_list(merged) == expected


def test_merge_sorted_lists_in_place_reuses_nodes():
    a = [1, 3, 5, 8]
    b = [2, 4, 6, 7, 9]
    l1 = build_list(a)
    l2 = build_list(b)

    ids1 = set(collect_node_ids(l1))
    ids2 = set(collect_node_ids(l2))
    merged = mergeSortedLists(l1, l2)

    merged_ids = collect_node_ids(merged)

    assert set(merged_ids) == ids1 | ids2

    assert len(merged_ids) == len(a) + len(b)


def test_merge_sorted_lists_no_cycle():
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    merged = mergeSortedLists(l1, l2)

    assert to_list(merged) == [1, 1, 2, 3, 4, 4]


def test_merge_sorted_lists_returns_same_head_when_one_empty():
    l1 = build_list([])
    l2 = build_list([1, 2, 3])
    merged = mergeSortedLists(l1, l2)

    assert merged is l2
    assert to_list(merged) == [1, 2, 3]

    l1 = build_list([4, 5])
    l2 = build_list([])
    merged = mergeSortedLists(l1, l2)
    assert merged is l1
    assert to_list(merged) == [4, 5]