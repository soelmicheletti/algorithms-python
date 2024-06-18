import random
import sys
from typing import List

def quick_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Quick Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    random.seed(42)
    def partition(nums: List[int], start: int, pivot: int, end: int) -> List[int]:
        l = start
        r = end
        while l <= r:
            while nums[l] < pivot:
                l += 1
            while nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l, r

    def quick_sort(nums: List[int], start: int, end: int) -> List[int]:
        if start >= end:
            return
        if start + 1 == end:
            if nums[start] > nums[end]:
                nums[start], nums[end] = nums[end], nums[start]
            return
        pivot = nums[random.randint(start, end)]
        l, r = partition(nums, start, pivot, end)
        quick_sort(nums, start, r)
        quick_sort(nums, l, end)
    quick_sort(nums, 0, len(nums) - 1)
    return nums

    