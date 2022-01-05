import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "value, expected", (([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0))
)
def test_solutions(value, expected):
    solution = Solution()
    assert solution.pivotIndex(value) == expected

    solution = Solution2()
    assert solution.pivotIndex(value) == expected
