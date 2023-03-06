"""
    33. Search in Rotated Sorted Array

    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot
    index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1],
    ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7]
    might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index
    of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    Example 3:

    Input: nums = [1], target = 0
    Output: -1


    Constraints:

    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10^4 <= target <= 10^4
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # check left side
        if nums[l] <= nums[mid]:
            # if target is out of left side array
            if target > nums[mid] or target < nums[l]:
                # move left pointer to the middle
                l = mid + 1
            else:
                r = mid - 1

        # check right side
        else:
            # check if target is between mid and right
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

    #     # split the array two part, check side by side
    #     # check in right side
    #     if nums[mid] > nums[r]:
    #         # check if target is between mid and right
    #         if target > nums[mid] or target < nums[r]:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #
    #     # check in left side
    #     else:
    #         # check if target is between left and mid
    #         if target < nums[mid] or target > nums[l]:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    # return -1




nums = [4,5,6,7,0,1,2]
print(search(nums, 0))

nums = [4,5,6,7,0,1,2]
print(search(nums, 3))

nums = [1]
print(search(nums, 0))

nums = [1, 3]
print(search(nums, 3))