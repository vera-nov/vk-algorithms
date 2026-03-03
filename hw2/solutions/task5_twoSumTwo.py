from typing import List

def twoSum(numbers: List[int], target: int) -> bool:
    l, r = 0, len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return True
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return False