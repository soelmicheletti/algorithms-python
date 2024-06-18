from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Bubble Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums