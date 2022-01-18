import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "value, expected", (([1, 1, 4, 2, 1, 3], 3), ([5, 1, 2, 3, 4], 5))
)
def test_solutions(value, expected):
    solution = Solution()
    assert solution.heightChecker(value) == expected
