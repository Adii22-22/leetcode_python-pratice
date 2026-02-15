# Problem: Toggle Light Bulbs
#
# Approach:
# We use a set to track bulbs that are currently ON.
#
# Logic:
# - If a bulb number appears for the first time, we turn it ON (add to set).
# - If it appears again, we turn it OFF (remove from set).
# - This works because toggling twice cancels out.
#
# The set naturally maintains bulbs that were toggled an odd number of times.
# At the end, we return the sorted list of bulbs that remain ON.
#
# Key Insight:
# A bulb remains ON only if it appears an odd number of times.
#
# Time Complexity: O(n log n)
#   - O(n) for toggling using set
#   - O(k log k) for sorting remaining ON bulbs
#
# Space Complexity: O(k)
#   - k = number of bulbs left ON
