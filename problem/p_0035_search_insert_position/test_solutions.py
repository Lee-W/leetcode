import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_nums, test_target, expected",
    (
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
    )
)
def test_solutions(test_nums, test_target, expected):
    solution = Solution()
    assert solution.searchInsert(test_nums, test_target) == expected
