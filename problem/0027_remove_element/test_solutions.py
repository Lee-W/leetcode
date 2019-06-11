import pytest

from solutions import Solution, Solution2


@pytest.mark.parametrize(
    "test_nums, test_val, expected_length, exptected_nums",
    [
        (
            [3, 2, 2, 3], 3, 2, [2, 2]
        ),
        (
            [0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]
        ),
        (
            [1, 1, 1, 1], 1, 0, []
        ),
        (
            [1, 1, 1, 1], 2, 4, [1, 1, 1, 1]
        )
    ]
)
def test_solutions(test_nums, test_val, expected_length, exptected_nums):
    solution = Solution()
    assert solution.removeElement(test_nums, test_val) == expected_length
    assert test_nums == exptected_nums

    solution2 = Solution2()
    assert solution2.removeElement(test_nums, test_val) == expected_length
    assert test_nums == exptected_nums
