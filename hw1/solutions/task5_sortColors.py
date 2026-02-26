from typing import List

def sortColors(nums: List[int]) -> None:
    n = len(nums)
    l, r, c = 0, n - 1, 0
    while c <= r:
        if nums[c] == 1:
            c += 1
        elif nums[c] == 0:
            nums[c], nums[l] = nums[l], nums[c]
            l += 1
            c += 1
        else:
            nums[c], nums[r] = nums[r], nums[c]
            r -= 1
