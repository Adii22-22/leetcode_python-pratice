# 169. Majority Element
# Solved on: Nov 22, 2025
#
# Approach: Boyer–Moore Majority Vote Algorithm (Optimal)
# -------------------------------------------------------
# We maintain a `candidate` and a `count`.
#
# Logic:
# - If count becomes 0, choose current number as new candidate.
# - If number == candidate → increase count.
# - Else → decrease count.
#
# Why this works?
# The majority element appears more than n/2 times.
# All other elements together cannot cancel its count completely.
#
# Time: O(n)
# Space: O(1)


