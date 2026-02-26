from typing import List

def moveEven(nums: List[int]) -> None:
    curr = 0
    z = 0
    while curr < len(nums):
        if nums[curr] % 2 == 0:
            nums[curr], nums[z] = nums[z], nums[curr]
            z += 1
        curr += 1
