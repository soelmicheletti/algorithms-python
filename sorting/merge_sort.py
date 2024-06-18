from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    """
       Sorting list with Merge Sort

       :param nums: list to be sorted
       :return: sorted list
    """
    def merge(a: List[int], b:List[int]) -> List[int]:
        l = 0
        r = 0
        res = []
        while l < len(a) and r < len(b):
            if a[l] <= b[r]:
                res.append(a[l])
                l += 1
            else:
                res.append(b[r])
                r += 1
        while l < len(a): 
            res.append(a[l])
            l += 1
        while r < len(b):
            res.append(b[r])
            r += 1
        return res
    
    def merge_sort(nums: List[int], start: int, end: int) -> List[int]:
        if start == end:
            return [nums[start]]
        if start + 1 == end:
            if nums[start] <= nums[end]:
                return [nums[start], nums[end]]
            return [nums[end], nums[start]]
        
        mid = (start + end) // 2
        left_list = merge_sort(nums, start, mid)
        right_list = merge_sort(nums, mid+1, end)
        return merge(left_list, right_list)
    return merge_sort(nums, 0, len(nums) - 1)
    