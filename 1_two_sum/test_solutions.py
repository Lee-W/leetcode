import pytest

from solutions import Solution, Solution2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ([2, 7, 11, 15], 9),
            [0, 1]
        ),
        (
            ([3, 2, 4], 6),
            [1, 2]
        )
    ]
)
def test_solution(test_input, expected):
    solution = Solution()
    assert solution.twoSum(*test_input) == expected

    solution = Solution2()
    assert solution.twoSum(*test_input) == expected
