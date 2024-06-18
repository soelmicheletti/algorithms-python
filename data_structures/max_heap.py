from typing import List
"""
library

import heapq
 
# Initialize a list with some values
values = [5, 1, 3, 7, 4, 2]
 
# Convert the list into a heap
heapq.heapify(values)
heapq.heappush(values, 6)
smallest = heapq.heappop(values)
"""

class MaxHeap():
    def __init__(self) -> None:
        self.arr = []
    
    def pop(self) -> int:
        if not len(self.arr):
            raise RuntimeError("Can not pop from empty heap!")
        res = self.arr[0]
        self.arr[0] = self.arr[-1]
        del self.arr[-1]
        self.max_heapify()
        return res
    
    def insert(self, val:int) -> None:
        self.arr.append(val)
        i = len(self.arr) - 1
        while i >= 0 and self.arr[i] > self.arr[i // 2]:
            self.arr[i], self.arr[i // 2] = self.arr[i // 2], self.arr[i]
            i = i // 2
    
    def max_heapify(self):
        i = 0
        while i < len(self.arr):
            max_child_val = self.arr[i]
            max_idx = i
            if 2 * i < len(self.arr) and self.arr[2 * i] > max_child_val:
                max_child_val = self.arr[2 * i]
                max_idx = 2 * i
            if 2 * i + 1 < len(self.arr) and self.arr[2 * i + 1] > max_child_val:
                max_child_val = self.arr[2 * i + 1]
                max_idx = 2 * i + 1
            if max_idx != i:
                self.arr[i], self.arr[max_idx] = self.arr[max_idx], self.arr[i]
                i = max_idx
            else:
                return