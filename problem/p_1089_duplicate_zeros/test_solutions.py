import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_arr, expected",
    (
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([0], [0]),
        ([], []),
    ),
)
def test_solutions(test_arr, expected):
    solution = Solution()
    solution.duplicateZeros(test_arr)

    assert test_arr == expected
