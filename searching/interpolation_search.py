from typing import List

def interpolation_search(nums: List[int], target: int) -> bool:
    """
       Searching for target in nums

       :param nums: list where serch is performed
       :param target: target to find in list
       :return: True iff target is in list
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        if left == right:
            return nums[left] == target
        t = (target - nums[left]) / (nums[right] - nums[left])
        if not (0 <= t <= 1):
            return False
        mid = int(left + t * (right - left))
        if nums[mid] == target:
            return True
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False