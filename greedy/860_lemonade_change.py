# LeetCode 860 - Lemonade Change
# https://leetcode.com/problems/lemonade-change/
#
# Approach:
# Use a greedy strategy by tracking the count of $5 and $10 bills.
# For each customer:
# - If the bill is $5, increase the count of $5 bills.
# - If the bill is $10, give one $5 as change if available.
# - If the bill is $20, prefer giving one $10 and one $5 as change;
#   otherwise, give three $5 bills if possible.
# If exact change cannot be provided at any step, return False.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool: # type: ignore
        bill_count_5 = 0
        bill_count_10 = 0
        for bill in bills:
            if bill == 5:  # for $5 bills no change needed
                bill_count_5 +=1
            elif bill == 10: # for $10 bills one $5 change needed
                if bill_count_5 >= 1:
                    bill_count_5 -= 1
                    bill_count_10 += 1
                else:
                    return False
            elif bill == 20: # for $20 bills prefer change  one $5 bill and $10 bill else  three $5 bills 
                if bill_count_5 >= 1 and bill_count_10 >= 1:
                    bill_count_5 -= 1
                    bill_count_10 -= 1
                else:
                    if bill_count_5 >=3:
                        bill_count_5 -= 3
                    else:
                        return False
        return True
