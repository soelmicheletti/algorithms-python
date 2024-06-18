from typing import List

def exponential_search(nums: List[int], target: int) -> bool:
    """
       Searching for target in nums

       :param nums: list where serch is performed
       :param target: target to find in list
       :return: True iff target is in list
    """
    left_limit = 1
    while left_limit < len(nums) and nums[left_limit] < target:
        left_limit *= 2
    if left_limit >= len(nums):
        return False
    
    right_limit = len(nums) - 1
    while nums[right_limit] > target and right_limit >= 2:
        right_limit = right_limit // 2

    left = left_limit
    right = right_limit
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False