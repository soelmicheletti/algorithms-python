import sys
from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Selection Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    for i in range(len(nums)):
        min_val = sys.maxsize
        min_pos = i
        for j in range(i, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_pos = j
        nums[i], nums[min_pos] = nums[min_pos], nums[i]
    return nums