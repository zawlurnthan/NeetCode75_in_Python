"""
    1. Two Sum

    Given an array of integers nums and an integer target, return indices of the two numbers
    such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the
    same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:

    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # create an empty dictionary
    prevMap = {}

    # to iterate with index i, use enumerate function
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        # assign n key with value i index
        prevMap[n] = i


nums = [2, 7, 11, 15]
print(twoSum(nums, 9))

nums = [3, 2, 4]
print(twoSum(nums, 6))

nums = [3, 3]
print(twoSum(nums, 6))
