# LeetCode 724 - Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
#
# Approach:
# First compute the total sum of the array.
# Maintain a running left sum while iterating through the array.
# At each index, calculate the right sum as:
# total_sum - left_sum - current_element.
# If left sum equals right sum, return the current index.
# Update left sum after checking the pivot condition.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
