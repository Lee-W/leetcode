import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "arr, expected",
    (
        ([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]),
        ([400], [-1]),
        ([400, 300], [300, -1]),
        ([3, 2, 100], [100, 100, -1]),
    ),
)
def test_solutions(arr, expected):
    solution = Solution()
    assert solution.replaceElements(arr) == expected
