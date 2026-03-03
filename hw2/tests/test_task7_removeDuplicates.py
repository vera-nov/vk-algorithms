from solutions.task7_removeDuplicates import removeDuplicates
import pytest
import random


def expected_unique_prefix(sorted_nums):
    """
    Create an array with all unique elements from the original array
    """
    if not sorted_nums:
        return []
    res = [sorted_nums[0]]
    for x in sorted_nums[1:]:
        if x != res[-1]:
            res.append(x)
    return res


@pytest.mark.parametrize(
    "nums",
    [
        [],
        [1],
        [1, 1, 1],
        [1, 2, 3, 4],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [-5, -5, -2, -2, -2, 0, 0, 3, 3, 10],
        [2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5],
    ],
)
def test_remove_duplicates_prefix(nums):
    original = nums.copy()
    expected = expected_unique_prefix(original)

    before_id = id(nums)
    ret = removeDuplicates(nums)
    assert ret is None
    assert id(nums) == before_id
    assert len(nums) == len(original)
    k = len(expected)
    assert nums[:k] == expected
    assert all(nums[i] < nums[i + 1] for i in range(max(0, k - 1)))


def test_already_unique_array_unchanged():
    nums = [1, 2, 3, 4, 5]
    original = nums.copy()
    removeDuplicates(nums)
    assert nums == original


def test_large_random_sorted():
    random.seed(0)
    nums = sorted(random.randint(-50, 50) for _ in range(2000))
    original = nums.copy()
    expected = expected_unique_prefix(original)

    removeDuplicates(nums)

    assert nums[: len(expected)] == expected
    assert len(nums) == len(original)