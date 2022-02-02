from typing import List


class Solution:
    """
    Runtime: 94 ms (48.84 %)
    Memory Usage: 14.1 MB (96.92 %)
    """

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])

        original_color = image[sr][sc]
        image[sr][sc] = newColor

        visited = [(sr, sc)]
        queue = [(sr, sc)]
        while queue:
            x, y = queue.pop(0)

            if (
                x + 1 < m
                and (x + 1, y) not in visited
                and image[x + 1][y] == original_color
            ):
                queue.append((x + 1, y))
                image[x + 1][y] = newColor
                visited.append((x + 1, y))

            if (
                y + 1 < n
                and (x, y + 1) not in visited
                and image[x][y + 1] == original_color
            ):
                queue.append((x, y + 1))
                image[x][y + 1] = newColor
                visited.append((x, y + 1))

            if (
                x - 1 > -1
                and (x - 1, y) not in visited
                and image[x - 1][y] == original_color
            ):
                queue.append((x - 1, y))
                image[x - 1][y] = newColor
                visited.append((x - 1, y))

            if (
                y - 1 > -1
                and (x, y - 1) not in visited
                and image[x][y - 1] == original_color
            ):
                queue.append((x, y - 1))
                image[x][y - 1] = newColor
                visited.append((x, y - y))

        return image


class Solution2:
    """
    Runtime: 76 ms (81.06 %)
    Memory Usage: 14 MB (99,24 %)
    """

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        """BFS"""
        m, n = len(image), len(image[0])

        original_color = image[sr][sc]
        image[sr][sc] = newColor

        queue = [(sr, sc)]
        visited = [(sr, sc)]
        while queue:
            x, y = queue.pop(0)
            up = (x - 1, y)
            down = (x + 1, y)
            left = (x, y - 1)
            right = (x, y + 1)

            for x, y in (up, down, left, right):
                if (
                    x > -1
                    and x < m
                    and y > -1
                    and y < n
                    and image[x][y] == original_color
                    and (x, y) not in visited
                ):
                    queue.append((x, y))
                    visited.append((x, y))
                    image[x][y] = newColor

        return image


class Solution3:
    """
    Runtime: 98 ms (46.32 %)
    Memory Usage: 14.1 MB (96.92 %)
    """

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]

        stack = [(sr, sc)]
        visited = [(sr, sc)]
        image[sr][sc] = newColor
        while stack:
            x, y = stack.pop()
            Solution3.visit_node(
                x, y, m, n, image, stack, visited, original_color, newColor
            )

        return image

    @staticmethod
    def visit_node(x, y, m, n, image, stack, visited, original_color, new_color):
        up = (x - 1, y)
        down = (x + 1, y)
        left = (x, y - 1)
        right = (x, y + 1)

        for x, y in (up, down, left, right):
            if (
                x > -1
                and x < m
                and y > -1
                and y < n
                and image[x][y] == original_color
                and (x, y) not in visited
            ):
                image[x][y] = new_color
                visited.append((x, y))
                Solution3.visit_node(
                    x, y, m, n, image, stack, visited, original_color, new_color
                )
        return
