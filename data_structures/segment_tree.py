# From Leetcode: 307. Range Sum Query - Mutable
class SegmentTree:
    def __init__(self, arr, lo, hi):
        self.sum = sum(arr[lo:hi+1])
        self.lower = lo
        self.upper = hi
        self.left = None
        self.right = None
        if lo == hi:
            return
        elif lo+1 == hi:
            self.left = SegmentTree(arr, lo, lo)
            self.right = SegmentTree(arr, hi, hi)
        else:
            m = (lo+hi) // 2
            self.left = SegmentTree(arr, lo, m)
            self.right = SegmentTree(arr, m+1, hi)
    
    def query(self, lo, hi):
        if lo <= self.lower and self.upper <= hi:
            return self.sum
        elif lo > (self.lower+self.upper) // 2:
            return self.right.query(lo, hi)
        elif hi <= (self.lower+self.upper) // 2:
            return self.left.query(lo, hi)
        else:
            return self.left.query(lo, (self.lower+self.upper) // 2)+self.right.query((self.lower+self.upper) // 2+1, hi)
    
    def update(self, index, delta):
        if self.lower == index and self.upper == index:
            self.sum += delta
        else:
            self.sum += delta
            if index <= (self.lower+self.upper) // 2:
                self.left.update(index, delta)
            else:
                self.right.update(index, delta)

class NumArray:

    def __init__(self, nums: List[int]):
        self.T = SegmentTree(nums, 0, len(nums)-1)
        self.arr = nums
        

    def update(self, index: int, val: int) -> None:
        delta = val-self.arr[index]
        self.arr[index] = val
        self.T.update(index, delta)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.T.query(left, right)