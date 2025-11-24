"""
412. Fizz Buzz
Difficulty: Easy
Date Solved: Nov 24, 2025

Approach:
- Loop from 1 to n.
- For each number:
    - If divisible by both 3 and 5 → "FizzBuzz"
    - If divisible by 3 → "Fizz"
    - If divisible by 5 → "Buzz"
    - Otherwise → convert number to string.
- Store results in an array and return it.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]: # type: ignore
        arr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr