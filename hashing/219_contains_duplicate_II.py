# ----------------------------------------------------------
# LeetCode 219 - Contains Duplicate II
# Category: Hashing
# Date Solved: 2025-12-12
# Logic:
#   - Maintain a dictionary that stores the last index 
#     where each number was seen.
#   - If the same number appears again and the index 
#     difference is <= k → duplicates are "nearby".
# ----------------------------------------------------------

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool: # type: ignore
        last_seen = {}

        for i in range(len(nums)):
            num = nums[i]

            # If we've seen this number before
            if num in last_seen:
                # Check distance between current and previous index
                if i - last_seen[num] <= k:
                    return True

            # Update last seen index
            last_seen[num] = i

        return False