from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    curr = m + n - 1
    ind1 = m - 1
    ind2 = n - 1
        
    while ind2 > -1:
        if ind1 > -1 and nums1[ind1] > nums2[ind2]:
            nums1[curr] = nums1[ind1]
            ind1 -= 1
        else:
            nums1[curr] = nums2[ind2]
            ind2 -= 1
        curr -= 1
        