import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "arr, expected",
    (
        ([10, 2, 5, 3], True),
        ([7, 1, 14, 11], True),
        ([3, 1, 7, 11], False),
        ([1, 2], True),
        ([0, 0], True),
        ([0, 1, 0], True),
        ([-2, 0, 10, -19, 4, 6, -8], False),
    ),
)
def test_solutions(arr, expected):
    solution = Solution()
    assert solution.checkIfExist(arr) is expected
