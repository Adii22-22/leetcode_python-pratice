# LeetCode 1047: Remove All Adjacent Duplicates In String
# Date solved: Dec 9, 2025
# Approach: Stack
# Explanation:
#   Iterate through each character and use a stack to remove adjacent duplicates.
#   If the current character matches the top of the stack, pop it (duplicate found).
#   Otherwise, push the character onto the stack.
#   The remaining stack contents form the final string with all adjacent duplicates removed.
# Time Complexity: O(n)       # each character is pushed/popped at most once
# Space Complexity: O(n)      # stack used to store non-duplicate characters
