import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "value, expected",
    (
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
        ([5, 2, 2], 5),
        ([1, 2, 2, 5, 3, 5], 2),
        ([3, 3, 4, 3, 4, 3, 0, 3, 3], 0),
    ),
)
def test_solutions(value, expected):
    solution = Solution()
    assert solution.thirdMax(value) == expected

    solution = Solution2()
    assert solution.thirdMax(value) == expected
