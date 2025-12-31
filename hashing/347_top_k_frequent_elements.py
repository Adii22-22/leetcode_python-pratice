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
import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: # type: ignore
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        sorted_map = sorted(count_map.items(),key=operator.itemgetter(1),reverse=True)

        result = []
        for number,freq in sorted_map:
            if len(result) >= k:
                break
            result.append(number)
        return result