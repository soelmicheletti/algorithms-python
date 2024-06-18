from .max_heap import MaxHeap
from typing import List

def heap_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Heap Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    heap = MaxHeap()
    for num in nums:
        heap.insert(num)
    sorted_list = []
    for _ in range(len(nums)):
        sorted_list.append(heap.pop())
    return sorted_list[::-1]