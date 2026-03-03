from solutions.task5_twoSumTwo import twoSum
import pytest

@pytest.mark.parametrize(
    "numbers, target, res",
    [
        ([1, 2, 3, 6], 5, True),
        ([1, 1, 1], 10, False),
        ([], 5, False),
        ([1], 1, False),
        ([1, 2], 3, True),
        ([1, 2], 4, False),
        ([1, 2, 2, 3, 4], 4, True),
        ([2, 2, 2, 2], 4, True),
        ([2, 2, 2, 2], 5, False),
        ([-5, -2, 0, 3, 7], 1, True),
        ([-5, -2, 0, 3, 7], -7, True),
    ],
)

def test_twoSum(numbers, target, res):
    assert twoSum(numbers, target) == res