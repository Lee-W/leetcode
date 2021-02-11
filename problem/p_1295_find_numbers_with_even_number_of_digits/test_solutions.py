import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_nums, expected", (([12, 345, 2, 6, 7896], 2), ([555, 901, 482, 1771], 1))
)
def test_solution(test_nums, expected):
    solution = Solution()
    assert solution.findNumbers(test_nums) == expected
