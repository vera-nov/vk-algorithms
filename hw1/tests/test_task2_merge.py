from solutions.task2_merge import merge


def test_merge_example():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_merge_with_empty():
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1, 2], []) == [1, 2]
    assert merge([], []) == []


def test_merge_with_duplicates():
    assert merge([1, 2, 2], [2, 2, 3]) == [1, 2, 2, 2, 2, 3]


def test_merge_negative_numbers():
    assert merge([-3, -1, 0], [-2, 2]) == [-3, -2, -1, 0, 2]


def test_merge_already_ordered_blocks():
    assert merge([1, 2, 3], [10, 11]) == [1, 2, 3, 10, 11]
    assert merge([10, 11], [1, 2, 3]) == [1, 2, 3, 10, 11]