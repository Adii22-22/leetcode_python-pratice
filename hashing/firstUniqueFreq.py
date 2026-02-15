# Problem: First Number With Unique Frequency
#
# Approach:
# 1. Use an OrderedDict to count the frequency of each number
#    while preserving insertion order.
#
# 2. Build a second dictionary (count_freq) to track how many
#    numbers share the same frequency.
#
# 3. Traverse the OrderedDict again:
#    - For each number, check its frequency.
#    - If that frequency appears only once in count_freq,
#      then this number has a unique frequency.
#    - Return the first such number (in insertion order).
#
# 4. If no such number exists, return -1.
#
# Key Insight:
# We are not looking for the first unique number,
# but the first number whose frequency itself is unique.
#
# Time Complexity: O(n)
#   - One pass to count frequencies
#   - One pass to count frequency-of-frequencies
#   - One pass to find answer
#
# Space Complexity: O(n)
#   - For frequency dictionary
#   - For count_freq dictionary
