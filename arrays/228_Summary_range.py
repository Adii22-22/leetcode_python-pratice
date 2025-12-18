# LeetCode 228 - Summary Ranges
#
# Approach:
# Iterate through the sorted array while tracking the start of a consecutive range.
# When the current number is not consecutive to the previous one, close the range
# by checking if it is a single number or a range, then store it.
# After the loop, handle the final range separately.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output list)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]: # type: ignore
        range_list = []
        if not nums:
            return range_list
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] +1:
                if start == nums[i-1]:
                    range_list.append(f"{start}")
                else:
                    number = f"{start}->{nums[i-1]}"
                    range_list.append(number)
                start = nums[i]
        
        if start ==  nums[-1]:
            range_list.append(f"{start}")
        else:
            number = f"{start}->{nums[-1]}"
            range_list.append(number)
        return range_list