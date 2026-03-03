from typing import List

def removeDuplicates(nums: List[int]) -> None:
    last = curr = 1
    while curr < len(nums):
        if nums[curr] != nums[curr - 1]:
            nums[last] = nums[curr]
            last += 1
        curr += 1
