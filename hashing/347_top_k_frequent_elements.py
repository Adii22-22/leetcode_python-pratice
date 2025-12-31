# LeetCode 347 - Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Approach:
# First, count the frequency of each element using a hash map.
# Then, sort the (element, frequency) pairs in descending order
# based on frequency.
# Finally, extract the first k elements from the sorted list.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the frequency map