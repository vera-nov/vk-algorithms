from typing import List

def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    def reverseArray(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverseArray(0, n - 1)
    reverseArray(0, k - 1)
    reverseArray(k, n - 1)