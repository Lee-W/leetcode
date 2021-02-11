import pytest

from .solutions import Solution


@pytest.mark.parametrize("test_nums, expected", (([1, 1, 0, 1, 1, 1], 3),))
def test_solutions(test_nums, expected):
    solution = Solution()
    assert solution.findMaxConsecutiveOnes(test_nums) == expected
