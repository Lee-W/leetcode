import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_nums, expected",
    (
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ),
)
def test_solution(test_nums, expected):
    solution = Solution()
    assert solution.sortedSquares(test_nums) == expected
