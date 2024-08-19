from typing import List
import random

def quick_select(arr: List[int], k: int):
    def quick_select_helper(k, left, right):
        #print(f"{left} {right} {k}")
        if left == right:
            return arr[left]
        if left+1 == right: 
            if k == 0: 
                return arr[left]
            return arr[right]
        pivot = random.choice(arr[left: right+1])
        l = left
        r = right
        while l <= r:
            while l < right-1 and arr[l] <= pivot: 
                l += 1
            while r > left and arr[r] > pivot: 
                r -= 1
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        if k < l: 
            return quick_select_helper(k, left, l)
        elif k == l:
            return arr[l]
        else: 
            return quick_select_helper(k - l - 1, l+1, right)
    return quick_select_helper(k, 0, len(arr)-1)
