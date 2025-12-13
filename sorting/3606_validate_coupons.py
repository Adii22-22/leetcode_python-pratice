"""
LeetCode 3606 — Validate Coupons

Approach:
- Iterate through code, businessLine, and isActive together.
- Filter out invalid coupons based on:
  • inactive status
  • empty code
  • non-alphanumeric / underscore characters
  • unsupported business line
- Store valid coupons as (businessLine, code) pairs.
- Sort coupons using a predefined business priority and then lexicographically by code.
- Return the sorted list of coupon codes.

Time Complexity:
O(n log n) due to sorting.

Space Complexity:
O(n) for storing valid coupons.
"""
