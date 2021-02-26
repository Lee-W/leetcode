import pytest

from .solutions import Solution, Solution2


@pytest.mark.parametrize(
    "test_nums, expected_length, exptected_nums",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 1, 1, 1], 1, [1]),
        ([], 0, []),
        (None, 0, None),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 1, 2], 2, [1, 2]),
    ],
)
def test_solution(test_nums, expected_length, exptected_nums):
    solution = Solution()
    assert solution.removeDuplicates(test_nums) == expected_length
    assert test_nums == exptected_nums

    solution = Solution2()
    assert solution.removeDuplicates(test_nums) == expected_length
    if expected_length:
        assert test_nums[:expected_length] == exptected_nums
    else:
        assert test_nums == exptected_nums
