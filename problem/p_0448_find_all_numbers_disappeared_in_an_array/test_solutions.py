import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize("nums, expected", (([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),))
def test_solutions(nums, expected):
    solution = Solution()
    assert solution.findDisappearedNumbers(nums) == expected

    solution = Solution2()
    assert solution.findDisappearedNumbers(nums) == expected
