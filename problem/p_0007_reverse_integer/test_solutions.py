import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    (
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (-1, -1),
        (-(2 ** 31) - 1, 0),
        (2 ** 31, 0),
        (1534236469, 0),
    ),
)
def test_solutions(test_input, expected):
    solution = Solution()
    assert solution.reverse(test_input) == expected
