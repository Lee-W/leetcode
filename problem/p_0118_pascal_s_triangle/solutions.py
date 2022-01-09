from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Runtime: 32 ms (66.53 %)
        Memory Usage: 14.3 MB
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        elif numRows == 3:
            return [[1], [1, 1], [1, 2, 1]]
        else:
            rows = [[1], [1, 1], [1, 2, 1]]
            for num in range(2, numRows - 1):
                tmp_row = [1, num + 1] + [
                    rows[num][i - 1] + rows[num][i] for i in range(2, num // 2 + 1)
                ]
                if num % 2:
                    tmp_row += [rows[num][num // 2] * 2]
                    tmp_row += [num for num in reversed(tmp_row[:-1])]
                else:
                    tmp_row += [num for num in reversed(tmp_row)]

                rows.append(tmp_row)

            return rows
