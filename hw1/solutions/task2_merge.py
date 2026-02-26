from typing import List
def merge(nums1: List[int], nums2: List[int]) -> List[int]:
    ind1, ind2 = 0, 0
    res = []
    
    while ind1 < len(nums1) and ind2 < len(nums2):
        if nums1[ind1] < nums2[ind2]:
            res.append(nums1[ind1])
            ind1 += 1
        else:
            res.append(nums2[ind2])
            ind2 += 1
    if ind1 < len(nums1):
        res.extend(nums1[ind1:])
    if ind2 < len(nums2):
        res.extend(nums2[ind2:])
    
    return res
