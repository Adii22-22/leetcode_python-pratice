# LeetCode 36 — Valid Sudoku
# Difficulty: Medium
# Solved on: Nov 19, 2025
#
# Approach:
# We use HashSets to track numbers seen in:
#   - each row
#   - each column
#   - each 3×3 sub-box
#
# If a number repeats in any of the three structures → not valid.
# This is a HashSet-based validation problem.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # type: ignore
        rows= [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}
        

        for row in range(len(rows)):
            for col in range(len(cols)):
                num = board[row][col]
                if num == ".":
                    continue
                else:
                    if num in rows[row]:
                        return False
                    else:
                        rows[row].add(num)
                    if num in cols[col]:
                        return False
                    else:
                        cols[col].add(num)

                    box_id = (row//3, col//3)
                    if box_id not in boxes:
                        boxes[box_id] = set()
                    if num in boxes[box_id]:
                        return False

                    boxes[box_id].add(num)
        return True

