"""Remove Element Kata from LeetCode"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """The solution to the Remove Element Kata
    that can be found at:
    https://leetcode.com/problems/remove-element/"""

    n = len(nums)
    idx = 0
    count = 0
    while idx < len(nums):
        if nums[idx] == val:
            nums.remove(nums[idx])
            count += 1
            idx = 0
        else:
            idx += 1
    return n - count
