import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "value, expected",
)
def test_solutions(value, expected):
    solution = Solution()
    assert solution.func(value) == expected
