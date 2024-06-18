import heapq
from typing import List

def heap_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Heap Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    heapq.heapify(nums)
    res = []
    for _ in range(len(nums)):
        res.append(heapq.heappop(nums))
    return res