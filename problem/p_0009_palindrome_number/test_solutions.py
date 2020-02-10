import pytest

from .solutions import Solution


@pytest.mark.parametrize(
    "test_input, expected",
    ((121, True), (-121, False), (10, False), (1, True), (-1, False), (12344321, True)),
)
def test_solutions(test_input, expected):
    solution = Solution()
    assert solution.isPalindrome(test_input) is expected
