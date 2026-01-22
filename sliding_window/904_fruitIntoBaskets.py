# LeetCode 904
# Problem: Fruit Into Baskets
# Link: https://leetcode.com/problems/fruit-into-baskets/
#
# Approach:
# Use a sliding window with two pointers (p1 and p2) and a hashmap (fruit_dict).
# The hashmap stores the count of each fruit type inside the current window.
#
# p2 expands the window by adding fruits one by one to the hashmap.
# If adding a fruit causes the number of distinct fruit types to exceed 2,
# move p1 forward to shrink the window.
#
# While shrinking, decrement the count of the fruit at p1 and remove it from
# the hashmap only when its count becomes zero.
#
# After restoring the window to a valid state (at most 2 fruit types),
# calculate the current window size using (p2 - p1 + 1) and update the maximum.
#
# Time Complexity: O(n) — each fruit is added and removed at most once
# Space Complexity: O(1) — hashmap stores at most 2 keys
class Solution:
    def totalFruit(self, fruits: List[int]) -> int: # type: ignore
        fruit_dict = {}
        p1= 0 
        win_length = 0

        for p2 in range(len(fruits)):
            if fruits[p2] in fruit_dict:
                fruit_dict[fruits[p2]]+=1
            else:
                fruit_dict[fruits[p2]]=1

            while len(fruit_dict) > 2:
                fruit_dict[fruits[p1]] -= 1
                if fruit_dict[fruits[p1]] == 0:
                    del fruit_dict[fruits[p1]]
                p1+=1
            win = p2-p1+1
            win_length = max(win_length,win)
        return win_length
