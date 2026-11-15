class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDigs = [set() for _ in range(9)]
        colDigs = [set() for _ in range(9)]
        boxDigs = [set() for _ in range(9)]

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val != ".":
                    b = (r // 3) * 3 + c // 3
                    # print(f"cell ({r}, {c}) in box {b} has {val}")
                    if val in rowDigs[r] or val in colDigs[c] or val in boxDigs[b]:
                        return False
                    rowDigs[r].add(val)
                    colDigs[c].add(val)
                    boxDigs[b].add(val)

        return True
                