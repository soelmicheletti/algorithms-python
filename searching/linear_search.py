from typing import List

def linear_search(nums: List[int], target: int) -> bool:
    """
       Searching for target in nums

       :param nums: list where serch is performed
       :param target: target to find in list
       :return: True iff target is in list
    """
    return target in nums