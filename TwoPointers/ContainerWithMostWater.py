"""
    11. Container With Most Water

    You are given an integer array height of length n. There are n vertical lines drawn such
    that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container
    contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Example 1:


    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
    this case, the max area of water (blue section) the container can contain is 49.

    Example 2:

    Input: height = [1,1]
    Output: 1

    Constraints:

    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4
"""
from typing import List


def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        # get max area by multiplying height and length
        # get min height between left and right
        # get length by subtracting from right to left
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            # move left pointer to the right for next calculation
            l += 1
        elif height[r] <= height[l]:
            # move right pointer to the left if it's less than left pointing value
            r -= 1
    return res



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# height = [1,1]
# print(maxArea(height))