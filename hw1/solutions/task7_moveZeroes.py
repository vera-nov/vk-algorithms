from typing import List

def moveZeroes(nums: List[int]) -> None:
    curr = 0
    z = 0
    while curr < len(nums):
        if nums[curr] != 0:
            nums[curr], nums[z] = nums[z], nums[curr]
            z += 1
        curr += 1
