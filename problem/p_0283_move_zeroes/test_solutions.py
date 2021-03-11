import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "nums, expected",
    (([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([-1, -1, 0], [-1, -1, 0])),
)
def test_solutions(nums, expected):
    solution = Solution()
    solution.moveZeroes(nums)
    assert nums == expected
