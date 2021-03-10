import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "arr, expected",
    (
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], False),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False),
        ([0, 1, 2, 4, 2, 1], True),
    ),
)
def test_solutions(arr, expected):
    solution = Solution()
    assert solution.validMountainArray(arr) is expected
