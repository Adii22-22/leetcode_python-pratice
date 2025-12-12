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