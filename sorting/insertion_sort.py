from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Insertion Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    for i in range(len(nums)):
        while i > 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            i -= 1
    return nums