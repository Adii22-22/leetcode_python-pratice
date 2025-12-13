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
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]: # type: ignore
        allowed_coupons = []
        priority = dict({"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3})
        for i,j,k in zip(code,businessLine,isActive):
            valid_code = all(c.isalnum() or c == "_" for c in i)
            if valid_code and  (len(i)> 0):
                if j in priority:
                    if k == True:
                        allowed_coupons.append([j,i])

        sorted_list = sorted(
            allowed_coupons,
            key=lambda x: (priority[x[0]], x[1])
        )
        return [x[1] for x in sorted_list]