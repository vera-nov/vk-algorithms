from solutions.task3_mergeSortedArrays import merge


def test_merge_sorted_arrays_example():
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_when_nums2_empty():
    nums1 = [1, 2, 3]
    merge(nums1, 3, [], 0)
    assert nums1 == [1, 2, 3]


def test_merge_when_nums1_has_no_initial_elements():
    nums1 = [0, 0, 0]
    merge(nums1, 0, [2, 5, 6], 3)
    assert nums1 == [2, 5, 6]


def test_merge_all_nums2_smaller():
    nums1 = [4, 5, 6, 0, 0, 0]
    merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_merge_with_duplicates():
    nums1 = [1, 2, 2, 0, 0]
    merge(nums1, 3, [2, 2], 2)
    assert nums1 == [1, 2, 2, 2, 2]