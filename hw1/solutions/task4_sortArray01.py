from typing import List

def sortArray01(nums: List[int]) -> None:
    n = len(nums)
    l, r = 0, n - 1
    while l < r:
        if nums[l] == 1:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1
